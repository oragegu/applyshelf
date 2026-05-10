from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import CoverLetter, EducationEntry, Experience, Language, RoleTrack, Snippet


def dashboard(request):
    context = {
        "snippet_count": Snippet.objects.count(),
        "experience_count": Experience.objects.count(),
        "education_count": EducationEntry.objects.count(),
        "cover_letter_count": CoverLetter.objects.count(),
        "recent_snippets": Snippet.objects.order_by("-updated_at")[:5],
    }
    return render(request, "applications/dashboard.html", context)


def snippet_list(request):
    snippets = Snippet.objects.all()
    search_query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()
    language = request.GET.get("language", "").strip()
    role_track = request.GET.get("role_track", "").strip()

    if search_query:
        snippets = snippets.filter(
            Q(title__icontains=search_query)
            | Q(category__icontains=search_query)
            | Q(content__icontains=search_query)
            | Q(notes__icontains=search_query)
        )
    if category:
        snippets = snippets.filter(category__iexact=category)
    if language:
        snippets = snippets.filter(language=language)
    if role_track:
        snippets = snippets.filter(role_track=role_track)

    context = {
        "snippets": snippets,
        "categories": Snippet.objects.order_by("category")
        .values_list("category", flat=True)
        .distinct(),
        "language_choices": Language.choices,
        "role_track_choices": RoleTrack.choices,
        "filters": {
            "q": search_query,
            "category": category,
            "language": language,
            "role_track": role_track,
        },
    }
    return render(request, "applications/snippet_list.html", context)


def snippet_detail(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    return render(request, "applications/snippet_detail.html", {"snippet": snippet})
