from django.urls import path

from . import views

urlpatterns = [
    path('contract/<int:id>/from_application', views.from_application),
    path('contract/<int:id>/one_query', views.one_query),
]