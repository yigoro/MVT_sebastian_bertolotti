from django.contrib import admin
from django.urls import path
from tp_django.views import hola

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', hola),
]
