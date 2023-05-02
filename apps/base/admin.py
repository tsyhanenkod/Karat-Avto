from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

@admin.register(BannerList)
class BannerAdmin(TranslationAdmin):
    list_display = ("id", "name", "get_image")
    list_display_links = ("name", "get_image")
    readonly_fields = ("get_image", )

    fieldsets = (
        ("Зображення", {
            "fields": (("image", "get_image"),)
        }),
        (None, {
            "fields": (("name"),)
        })
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="420" height="90">')

    get_image.short_description = "Зображення"

admin.site.site_title = "Автосалон Karat-Avto"
admin.site.site_header = "Автосалон Karat-Avto"
