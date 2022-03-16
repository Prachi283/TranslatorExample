from django.contrib import admin
from django.urls import path, include

from translator_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('i18n/', include('django.conf.urls.i18n')),
]