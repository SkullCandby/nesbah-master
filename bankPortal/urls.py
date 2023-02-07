from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path('portal/', views.main, name='bankportal'),
    path('see-full-data/', views.see_full_data, name='fulldata'),
    path('view_application/', views.application_viewed, name='fulldata'),
    path('history/', views.history, name='history'),
] + static("/", document_root=settings.STATIC_ROOT)