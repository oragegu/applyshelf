from django.urls import path

from . import views

app_name = "applications"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("snippets/", views.snippet_list, name="snippet_list"),
    path("snippets/<int:pk>/", views.snippet_detail, name="snippet_detail"),
]
