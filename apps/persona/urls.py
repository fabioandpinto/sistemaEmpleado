from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'persona_app'

urlpatterns = [

    path('', views.StartView.as_view(), name='inicio'),
    # urls of proof
    path(
        'listar/',
        views.ListAllEmpleados.as_view(),
        name='all'
    ),
    path(
        'listar_por/<depart>/',
        views.ListByArea.as_view(),
        name='por_area'
    ),
    path('buscar/', views.GetList.as_view()),
    path(
        'detalle/<pk>',
        views.DetailEmpleado.as_view(),
        name='detail',
    ),
    path(
        'nuevo/',
        views.CreateEmployee.as_view(),
        name='crear'
    ),
    path('success/', views.SuccessView.as_view(), name='correct'),
    path(
        'update/<pk>',
        views.UpdateEmployee.as_view(),
        name='update'
    ),
    path(
        'delete/<pk>',
        views.DeleteEmployee.as_view(),
        name='delete'
    ),
    path(
        'admin_empleados/',
        views.AdminEmpleados.as_view(),
        name='administrador',
    )
]
