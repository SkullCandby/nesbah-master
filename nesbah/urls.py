"""nesbah URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from nesbah import views

urlpatterns = [
    path('', views.main, name='home'),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('admin_portal/', include('adminPortal.urls')),
    path('bank/', include('bankPortal.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#add this to urlpatterns variable

