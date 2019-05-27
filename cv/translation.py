from modeltranslation.translator import translator, TranslationOptions
from .models import Skill, Shool, Testimonial, Work, Duty


class SkillTranslationOptions(TranslationOptions):
    fields = ("name",)


class ShoolTranslationOptions(TranslationOptions):
    fields = ("name", "endTitle")


class TestimonialTranslationOptions(TranslationOptions):
    fields = ("project", "testimonial")


class WorkTranslationOptions(TranslationOptions):
    fields = ("company", "position")


class DutyTranslationOptions(TranslationOptions):
    fields = ("description",)


translator.register(Skill, SkillTranslationOptions)
translator.register(Shool, ShoolTranslationOptions)
translator.register(Testimonial, TestimonialTranslationOptions)
translator.register(Work, WorkTranslationOptions)
translator.register(Duty, DutyTranslationOptions)
