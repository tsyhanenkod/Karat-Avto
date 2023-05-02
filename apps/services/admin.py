from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ("id", "name")
    list_display_links = ("name", )

    fieldsets = (
        ("", {
            "fields": (("service_image"),)
        }),
        ("", {
            "fields": (("name"),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.service_image.url} width="450" height="60" object-fit="cover">')
