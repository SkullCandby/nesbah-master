from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path('portal/', views.main, name='bankportal'),
    path('see-full-data/', views.see_full_data, name='fulldata'),
    path('history/', views.main, name='history'),
] + static("/", document_root=settings.STATIC_ROOT)