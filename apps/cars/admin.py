from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin

class CarAdminForm(forms.ModelForm):
    description_en = forms.CharField(label="Опис en", widget=CKEditorUploadingWidget())
    description_uk = forms.CharField(label="Опис uk", widget=CKEditorUploadingWidget())
    class Meta:
        model = Car
        fields = 'description_uk', 'description_en'


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name", "url")


@admin.register(EngineTypes)
class EngineTypesAdmin(TranslationAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name", "url")


@admin.register(Transmission)
class TransmissionAdmin(TranslationAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name", "url")


@admin.register(Colors)
class ColorsAdmin(TranslationAdmin):
    list_display = ("id", "name", "hex", "url")
    list_display_links = ("name", "hex", "url")


@admin.register(CarMark)
class CarMarkAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name", "url")


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "mark", "url")
    search_fields = ("name",)
    list_filter = ("mark",)
    list_display_links = ("name", "mark", "url")


@admin.register(DriveUnit)
class DriveUnitAdmin(TranslationAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name", "url")


@admin.register(BodyType)
class BodyTypeAdmin(TranslationAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name", "url")

class CarImagesInLine(admin.TabularInline):
    model = CarImages
    extra = 1
    list_display = ("id", "get_image", "name", "car")
    readonly_fields = ("get_image",)

    fieldsets = (
        (None, {
            "fields": (("image", "get_image"),)
        }),
        (None, {
            "fields": (("name", "car"),)
        })
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="92" height="60">')

    get_image.short_description = "Зображення"


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("id", "get_image", "mark", "model", "engine_type", "price", "year", "url", "draft")
    list_filter = ("mark", "year", "draft")
    list_display_links = ("mark", "model", "get_image")
    search_fields = ("mark__name", "model__name", "name")
    readonly_fields = ("get_image",)
    inlines = [CarImagesInLine, ]
    form = CarAdminForm
    actions = ["publish", "unpublish"]
    save_on_top = True
    list_editable = ("draft",)
    fieldsets = (
        ("Зображення", {
            "fields": (("main_image", "get_image"), )
        }),
        ("Загальні", {
           "fields": (("mark", "model", "category", "year"), )
        }),
        ("Опис", {
            "fields": (("description_uk", "description_en",),)
        }),
        ("Ціна", {
            "fields": (("price"),)
        }),
        ("Характеристики", {
            "fields": (("car_weight", "engine_type", "engine_volume", "power", ),
                       ("car_speeds", "transmission", "drive_unit", ),
                       )
        }),
        ("Кузов", {
            "fields": (("dimensions", "body_type", "color"),)
        }),
        ("Опції", {
            "fields": (("url", "draft"),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.main_image.url} width="95" height="70" object-fit="cover">')

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


@admin.register(CarImages)
class CarImagesAdmin(TranslationAdmin):
    list_display = ("id", "get_image", "name", "car")
    list_display_links = ("get_image", 'name', "car")
    list_filter = ("car", )
    readonly_fields = ("get_image", )

    fieldsets = (
        ("Зображення", {
            "fields": (("image", "get_image"), )
        }),
        (None, {
            "fields": (("name", "car"),)
        })
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="92" height="60">')

    get_image.short_description = "Зображення"

