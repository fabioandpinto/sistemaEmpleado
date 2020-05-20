from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'departamento'

urlpatterns = [
    path(
        'nuevo_departamento/',
         views.NewDepartmentView.as_view(),
        name='newDepartamento'
    ),
    path(
        'listar_departamentos/',
         views.ListDepartamento.as_view(),
        name='lista_departamentos'
    ),
]