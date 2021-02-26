from django.urls import path, include
from rest_framework import routers
from .views import GameView

router = routers.DefaultRouter()

urlpatterns = [
    path('games/', GameView.as_view()),
]
