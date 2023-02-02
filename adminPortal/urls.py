from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.main, name='adminportal'),
    path('leads/', views.leads, name='leads'),
    path('users/', views.users, name='users'),
] + static("/", document_root=settings.STATIC_ROOT)