from django.db import models


class Language(models.TextChoices):
    ENGLISH = "english", "English"
    FRENCH = "french", "French"


class RoleTrack(models.TextChoices):
    DATA = "data", "Data"
    BACKEND_PLATFORM = "backend_platform", "Backend/Platform"
    ML_DATA_SCIENCE = "ml_data_science", "ML/Data Science"
    DEVOPS_SERVICE_OPS = "devops_service_ops", "DevOps/Service Ops"
    GENERAL_IT = "general_it", "General IT"
    OTHER = "other", "Other"


class Snippet(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    language = models.CharField(max_length=20, choices=Language.choices)
    role_track = models.CharField(max_length=40, choices=RoleTrack.choices)
    content = models.TextField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    ongoing = models.BooleanField(default=False)
    language = models.CharField(max_length=20, choices=Language.choices)
    role_track = models.CharField(max_length=40, choices=RoleTrack.choices)
    description = models.TextField()
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-start_date", "title"]

    def __str__(self):
        return f"{self.title} at {self.organization}"


class EducationEntry(models.Model):
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["-start_year", "school"]
        verbose_name_plural = "education entries"

    def __str__(self):
        return f"{self.degree} - {self.school}"


class CoverLetter(models.Model):
    class Status(models.TextChoices):
        APPLIED = "applied", "Applied"
        INTERVIEW = "interview", "Interview"
        REJECTED = "rejected", "Rejected"
        OFFER = "offer", "Offer"
        WITHDRAWN = "withdrawn", "Withdrawn"

    company = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    application_date = models.DateField()
    role_track = models.CharField(max_length=40, choices=RoleTrack.choices)
    cover_letter_text = models.TextField()
    key_claims = models.TextField(blank=True)
    interview_prep_notes = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.APPLIED,
    )

    class Meta:
        ordering = ["-application_date", "company"]

    def __str__(self):
        return f"{self.company} - {self.job_title}"
