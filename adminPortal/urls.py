from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.main, name='main'),
] + static("/", document_root=settings.STATIC_ROOT)