import nested_admin
from django.contrib import admin

from .models import (
    ExperienceUnit,
    Language,
    Link,
    PWBUnit,
    Skill,
    Project,
    ProjectLink,
)


class SkillInline(nested_admin.NestedTabularInline):
    model = Skill
    extra = 1


class ExperienceUnitInline(nested_admin.NestedTabularInline):
    model = ExperienceUnit
    extra = 1


class LinkInline(nested_admin.NestedTabularInline):
    model = Link
    extra = 1


class LanguageInline(nested_admin.NestedTabularInline):
    model = Language
    extra = 1


class ProjectLinkInline(nested_admin.NestedTabularInline):
    model = ProjectLink
    extra = 1

class ProjectInline(nested_admin.NestedTabularInline):
    model = Project
    extra = 1
    inlines = [ProjectLinkInline]

@admin.register(PWBUnit)
class PWBUnitAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        SkillInline,
        LinkInline,
        LanguageInline,
        ExperienceUnitInline,
        ProjectInline,
    ]
