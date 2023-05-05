from django.contrib import admin
from .models import *
from django import forms
from modeltranslation.admin import TranslationAdmin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.functional import cached_property

@admin.register(Char)
class CharAdmin(TranslationAdmin):
    list_display = ("id", "name", "char_category")
    list_filter = ("char_category",)
    list_display_links = ("id", "name",)

class ValuesInline(admin.TabularInline):
    model = Values
    extra = 0

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        if obj:
            char_list = [char.name for char in obj.char.all()]
            formset.form.base_fields['char'].queryset = Char.objects.filter(name__in=char_list)
            self.extra = len(char_list)
        return formset

    def save_formset(self, request, form, formset, change):
        super().save_formset(request, form, formset, change)
        for form in formset.forms:
            values_obj = form.instance
            complect_obj = values_obj.complect
            for char_value in complect_obj.char.all():
                char_value_str = char_value.name.lower().replace(' ', '_')
                value = form.cleaned_data.get(char_value_str, None)
                if value is not None:
                    char_value_obj, created = Char.objects.get_or_create(name=char_value.name)
                    char_value_obj.values.add(values_obj)
                    setattr(values_obj, f'{char_value_str}_value', value)
                    values_obj.save()




class PricesInline(admin.TabularInline):
    model = Prices
    extra = 0

@admin.register(Complect)
class ComplectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {
            'widget': FilteredSelectMultiple('Char, Charcategory', is_stacked=False)
        },
    }

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
