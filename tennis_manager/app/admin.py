from django.contrib import admin

from app.models import Field, Match, User

admin.site.register([User, Match, Field])
