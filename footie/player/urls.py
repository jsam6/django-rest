from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.getAllPlayer),
    path('create/', views.createPlayer),
]
