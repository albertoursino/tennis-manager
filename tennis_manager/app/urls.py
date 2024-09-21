from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("users", views.users, name="users"),
    path("user", views.user, name="user"),
    path("matches", views.matches, name="matches"),
    path("match", views.match, name="match"),
    path("fields", views.fields, name="fields"),
]
