from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', )