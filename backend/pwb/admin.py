from django.contrib import admin
from .models import PWBUnit, Skill


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


@admin.register(PWBUnit)
class PWBUnitAdmin(admin.ModelAdmin):
    inlines = [SkillInline]
