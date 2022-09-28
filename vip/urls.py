from django.urls import path
from vip import views

urlpatterns = [
    path('membre/', views.membre_view, name='membre_view'),
    path('vip-json/', views.post_vip_json, name='vip_post_json'),
]


