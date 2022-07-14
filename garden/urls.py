from django.urls import path

from garden import views

urlpatterns = [
    path('', views.main)
]