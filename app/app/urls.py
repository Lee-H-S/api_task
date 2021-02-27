"""
URLs for the API
"""

from django.urls import path, include

urlpatterns = [
    path("api/", include("core.urls")),
    path("users/", include("users.urls")),
]
