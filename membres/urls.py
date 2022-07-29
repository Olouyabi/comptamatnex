from django.urls import path
from membres import views

urlpatterns = [
    path('membre/', views.membre_view, name='membre_view'),
]
