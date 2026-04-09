from django.contrib import admin

from .models import ExperienceUnit, Language, Link, PWBUnit, Skill


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


class ExperienceUnitInline(admin.TabularInline):
    model = ExperienceUnit
    extra = 1


class LinkInline(admin.TabularInline):
    model = Link
    extra = 1


class LanguageInline(admin.TabularInline):
    model = Language
    extra = 1


@admin.register(PWBUnit)
class PWBUnitAdmin(admin.ModelAdmin):
    inlines = [SkillInline, LinkInline, LanguageInline, ExperienceUnitInline]
