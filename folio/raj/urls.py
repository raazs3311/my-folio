from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'raj'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('raaz', views.base, name = 'base'),
    path('', views.raaz, name = 'raaz'),
    path('contact', views.contact, name = 'contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)