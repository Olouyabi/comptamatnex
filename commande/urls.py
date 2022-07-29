from django.urls import path
from commande import views

urlpatterns = [
    path('store/', views.store, name='store_view'),
    path('store/version/<slug:version>/', views.store, name='store_version_livre'),
    path('panier/', views.panier, name='panier_view'),
    path('validation/', views.validation, name='validation_view'),
    path('mouvement_article/', views.mouvement_article, name='mouvement_article'),
    path('payement/', views.process_order, name='payement'),
]
