from modeltranslation.translator import register, TranslationOptions
from .models import Citys, ObjectsDetail


@register(Citys)
class EnterprisesTranslationOptions(TranslationOptions):
    fields = ('text', 'descriptions', 'descriptions_1')


@register(ObjectsDetail)
class RepairTranslationOptions(TranslationOptions):
    fields = ('description',)
