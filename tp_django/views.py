from django.http import HttpResponse
from django.template import loader, Template, Context
from mvt_familiares.models import Familiar

def template_using_loader(self, name: str ='name', last_name: str = 'last_name'):
    template = loader.get_template('template_loader.html')

    context_dict = {'name': name,
                    'last_name': last_name
                    }
    render = template.render(context_dict)
    return HttpResponse(render)

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

    familiar.save() #Esto guarda en la base de datos

    context_dict = {'familiar': familiar}

    render = template.render(context_dict)
    return HttpResponse(render)
