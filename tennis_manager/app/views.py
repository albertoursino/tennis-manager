from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from app import models


def home(request: HttpRequest) -> HttpResponse:
    """Render the main view of the website."""
    return render(request, "app/home.html", context={})


def users(request: HttpRequest) -> HttpResponse:
    """List of users view."""
    return render(request, "app/users.html", context={"users": models.User.objects.all()})


def user(request: HttpRequest) -> HttpResponse:
    """User view."""
    return render(request, "app/user.html", context={})


def matches(request: HttpRequest) -> HttpResponse:
    """List of matches view."""
    return render(request, "app/matches.html", context={})


def match(request: HttpRequest) -> HttpResponse:
    """Match view."""
    return render(request, "app/match.html", context={})


def fields(request: HttpRequest) -> HttpResponse:
    """List of fields view."""
    return render(request, "app/fields.html", context={})
