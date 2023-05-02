from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin


class ProductAdminForm(forms.ModelForm):
    description_uk = forms.CharField(label="Опис", widget=CKEditorUploadingWidget())
    description_en = forms.CharField(label="Опис eng", widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name_uk", "name_en", "get_image",)
    list_display_links = ("name_uk", "name_en", )
    readonly_fields = ("get_image", )
    search_fields = ("name_uk", "name_en", )
    form = ProductAdminForm
    actions = ["publish", "unpublish"]

    fieldsets = (
        ("Зображення", {
            "fields": (("product_image", "get_image"),)
        }),
        ("", {
            "fields": (("name_uk", "name_en", ),)
        }),
        ("Опис", {
            "fields": (("description_uk",),)
        }),
        ("Опис ENG", {
            "fields": (("description_en",),)
        }),
        ("Опції", {
            "fields": (("draft"),)
        }),
    )
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.product_image.url} width="92" height="60" object-fit="cover">')

    def unpublish(self, request, queryset):
        row_update = queryset.update(draft=False)
        if row_update == 1:
            massege_bit = f"1 запис було оновлено"
        else: massege_bit = f"{row_update} записи було оновлено"
        self.message_user(request, f"{massege_bit}")

    def publish(self, request, queryset):
        row_update = queryset.update(draft=True)
        if row_update == 1:
            massege_bit = f"1 запис було оновлено"
        else: massege_bit = f"{row_update} записи було оновлено"
        self.message_user(request, f"{massege_bit}")

    publish.short_description = "Зняти з публікації"
    publish.allowed_permissions = ('change', )

    unpublish.short_description = "Опублікувати"
    unpublish.allowed_permissions = ('change',)

    get_image.short_description = "Зображення"