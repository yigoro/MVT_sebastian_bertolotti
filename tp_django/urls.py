from django.contrib import admin
from django.urls import path
from tp_django.views import (
    nuevo_familiar,
    mostrar_familiares,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nuevo_familiar/<str:nombre>/<str:apellido>/<str:parentezco>/<int:dni>', nuevo_familiar),
    path('mostrar_familiares/', mostrar_familiares),
]

