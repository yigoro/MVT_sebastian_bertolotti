from django.contrib import admin
from django.urls import path
from tp_django.views import (
    template_using_loader,
    nuevo_familiar,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('template_using_loader/<str:name>/<str:last_name>', template_using_loader),
    path('nuevo_familiar/<str:nombre>/<str:apellido>/<str:parentezco>/<str:fecha_nacimiento>/<str:dni>', nuevo_familiar),
]

