from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(BannerList)
class BannerListTranslationOptions(TranslationOptions):
    fields = ('name', )