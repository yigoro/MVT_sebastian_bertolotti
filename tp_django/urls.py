from django.contrib import admin
from django.urls import path
from tp_django.views import (
    nuevo_familiar,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nuevo_familiar/<str:nombre>/<str:apellido>/<str:parentezco>/<str:fecha_nacimiento>/<str:dni>', nuevo_familiar),
]

