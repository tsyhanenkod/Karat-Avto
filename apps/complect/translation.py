from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Charcategory)
class CharcategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Complect)
class ComplectTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Char)
class CharTranslationOptions(TranslationOptions):
    fields = ('name', )