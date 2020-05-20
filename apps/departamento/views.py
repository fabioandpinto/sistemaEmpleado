from django.shortcuts import render

# for forms with various forms
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .forms import NewDepartmentForm

# models
from apps.persona.models import Empleado
from .models import Departamento


class ListDepartamento(ListView):
    model = Departamento
    template_name = "departamento/listDepartament.html"
    context_object_name = 'departamento'


# Create your views here.
class NewDepartmentView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartmentForm
    success_url = '/'

    def form_valid(self, form):
        print('***** form valid *****')
        depa = Departamento(
            name=form.cleaned_data['department'],
            short_name=form.cleaned_data['short_name'],
            type=form.cleaned_data['type'],
            is_active=form.cleaned_data['is_active'],
        )
        depa.save()
        name = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            department=depa,
            first_name=name,
            last_name=apellido,
            position='Directivo',
        )
        return super().form_valid(form)
