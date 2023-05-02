from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(EngineTypes)
class EngineTypesTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Transmission)
class TransmissionTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Colors)
class ColorsTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(DriveUnit)
class DriveUnitTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(BodyType)
class BodyTypeTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(CarImages)
class CarImagesTranslationOptions(TranslationOptions):
    fields = ('name', )

