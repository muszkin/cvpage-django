from django.contrib import admin

# Register your models here.

from .models import Skill, Shool, Testimonial, Work, Duty
from modeltranslation.admin import TranslationAdmin


class SkillAdmin(TranslationAdmin):
    pass


class ShoolAdmin(TranslationAdmin):
    pass


class TestimonialAdmin(TranslationAdmin):
    pass


class WorkAdmin(TranslationAdmin):
    pass


class DutyAdmin(TranslationAdmin):
    pass


admin.site.register(Shool, ShoolAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Duty, DutyAdmin)
