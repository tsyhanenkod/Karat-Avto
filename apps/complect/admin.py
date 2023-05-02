from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(Char)
class CharAdmin(TranslationAdmin):
    list_display = ("id", "name", "char_category")
    list_filter = ("char_category",)
    list_display_links = ("id", "name",)

class ValuesInline(admin.TabularInline):
    model = Values


class PricesInline(admin.TabularInline):
    model = Prices

@admin.register(Complect)
class ComplectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "car",)
    list_display_links = ("id", "name",)
    list_filter = ("car", )
    search_fields = ("name", "car")
    inlines = [PricesInline, ValuesInline, ]
    save_on_top = True
    save_as = True





class ComplectAdmin(TranslationAdmin):
    inlines = [ValuesInline, PricesInline]

admin.site.register(Charcategory)
