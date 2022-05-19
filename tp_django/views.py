from django.http import HttpResponse
from django.template import loader, Template, Context
from mvt_familiares.models import Familiar
from datetime import datetime

def nuevo_familiar(self,
    nombre: str ='',
    apellido: str = '',
    parentezco: str = '',
    dni: int = 0):

    template = loader.get_template('template_familiar.html')

    familiar = Familiar(nombre=nombre,
                        apellido=apellido,
                        parentezco=parentezco,
                        dni=dni)

    familiar.save() #Este comando graba en la DDBB

    context_dict = {'familiar': familiar}

    render = template.render(context_dict)
    return HttpResponse(render)

def mostrar_familiares(self):
    template = loader.get_template('template_listado.html')
    familiar = Familiar.objects.all()

    fecha = datetime.now()
    context_dict = {'familiares': familiar, 'fecha': fecha}

    render = template.render(context_dict)
    return HttpResponse(render)