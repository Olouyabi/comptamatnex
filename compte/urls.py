from django.urls import path
from compte import views

urlpatterns = [
    path('compte/login/', views.login_view, name='login_view'),
    path('compte/logout/', views.logout_view, name='logout_view'),
]
