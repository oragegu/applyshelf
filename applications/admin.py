from django.contrib import admin

from .models import CoverLetter, EducationEntry, Experience, Snippet


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "language", "role_track", "updated_at")
    list_filter = ("category", "language", "role_track")
    search_fields = ("title", "content", "notes")


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "organization",
        "location",
        "start_date",
        "end_date",
        "ongoing",
        "language",
        "role_track",
    )
    list_filter = ("language", "role_track", "ongoing")
    search_fields = ("title", "organization", "description", "notes")


@admin.register(EducationEntry)
class EducationEntryAdmin(admin.ModelAdmin):
    list_display = ("school", "degree", "field_of_study", "start_year", "end_year")
    search_fields = ("school", "degree", "field_of_study", "description")


@admin.register(CoverLetter)
class CoverLetterAdmin(admin.ModelAdmin):
    list_display = ("company", "job_title", "application_date", "role_track", "status")
    list_filter = ("role_track", "status", "application_date")
    search_fields = (
        "company",
        "job_title",
        "cover_letter_text",
        "key_claims",
        "interview_prep_notes",
    )
