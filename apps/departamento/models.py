from django.db import models


# Create your models here.
class Departamento(models.Model):
    type = (
        ('O', 'Operativo'),
        ('A', 'Administrativo'),
    )

    name = models.CharField('Nombre', max_length=50, unique=True)
    short_name = models.CharField('Nombre corto', max_length=50, blank=True)
    type = models.CharField('Area', choices=type, max_length=50)
    is_active = models.BooleanField('Activo')

    def __str__(self):
        return self.name
