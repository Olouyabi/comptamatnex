"""comptamatnex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views
from comptamatnex.settings import STATIC_URL
from . import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns



urlpatterns = [
    path('', views.home, name="home_view"),
    path('contact/', views.contact, name="contact_view"),
    path('', include('blog.urls')),
    path('', include('compte.urls')),
    path('', include('membres.urls')),
    path('', include('commande.urls')),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

