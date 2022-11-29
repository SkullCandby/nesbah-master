from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('index/', views.index, name='home'),
    path('employee/', views.employee, name='employee'),
    path('activate/(?P<uidb64>+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        views.activate, name='activate'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)