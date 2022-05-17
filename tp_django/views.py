from django.http import HttpResponse
from django.template import loader, Template, Context
from mvt_familiares.models import Familiar

def nuevo_familiar(self,
                        nombre: str ='mariano',
                        apellido: str = 'bertolotti',
                        parentezco: str = 'hermano',
                        fecha_nacimiento: str = '27-11-1982',
                        dni: str = '12345678'):

    template = loader.get_template('template_familiar.html')

    familiar = Familiar(nombre=nombre,
                        apellido=apellido,
                        parentezco=parentezco,
                        fecha_nacimiento=fecha_nacimiento,
                        dni=dni)

    familiar.save() #Este comando graba en la DDBB

    context_dict = {'familiar': familiar}

    render = template.render(context_dict)
    return HttpResponse(render)
