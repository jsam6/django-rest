from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # ex: /player/5/
    # path("<int:question_id>/", views.player_detail, name="player_detail"),
]