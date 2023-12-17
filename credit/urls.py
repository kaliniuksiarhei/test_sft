from django.urls import path

from . import views

urlpatterns = [
    path('contracts/<int:id>/manufacturers', views.get_unique_manufacturers),
]
