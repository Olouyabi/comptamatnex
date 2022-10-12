from django import views
from django.urls import path
from blog import views


urlpatterns = [
    path('blog/', views.post_list, name="post_list"),
    path('blog/category/<slug:category>/', views.post_list, name="category_post_list"),
    path('blog/<int:day>/<int:month>/<int:year>/<slug>/', views.post_detail, name="post_detail"),
    path('recherche/', views.recherche_post, name='recherche_post'),
]
