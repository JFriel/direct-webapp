"""Admin module for the main app."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin

from .models import Category, Skill, SkillLevel, User, UserSkill

admin.site.register(User, UserAdmin)


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin,admin.ModelAdmin[Category]):
    """Admin class for the Category model."""

    list_display = ("name", "description", "parent_category")
    search_fields = ("name", "description")
    list_filter = ("parent_category",)
    ordering = ("name",)


@admin.register(Skill)
class SkillAdmin(ImportExportModelAdmin,admin.ModelAdmin[Skill]):
    """Admin class for the Skill model."""

    list_display = ("name", "description", "category")
    search_fields = ("name", "description")
    list_filter = ("category",)
    ordering = ("name",)


@admin.register(SkillLevel)
class SkillLevelAdmin(ImportExportModelAdmin,admin.ModelAdmin[SkillLevel]):
    """Admin class for The SkillLevel model."""

    list_display = ("name", "level")
    search_fields = ("name",)


@admin.register(UserSkill)
class UserSkillAdmin(ImportExportModelAdmin,admin.ModelAdmin[UserSkill]):
    """Admin class for The UserSkill model."""

    list_display = ("user", "skill", "skill_level")
    search_fields = ("user", "skill")
