from django.db import models
import apps.departamento.models as model


# Create your models here.


class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=30)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'


class Empleado(models.Model):
    """ Modelo para la tabla empleado"""
    level = (
        ('Directivo', 'Directivo'),
        ('Asesor', 'Asesor'),
        ('Operativo', 'Operativo'),
        ('Tecnico', 'Tecnico'),
        ('Asistencial', 'Asistencial'),
    )
    department = models.ForeignKey(model.Departamento, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, verbose_name="Nombre")
    last_name = models.CharField(max_length=50, verbose_name="Apellido")
    position = models.CharField(choices=level, max_length=50)
    avatar = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return self.first_name + ' - ' + self.last_name
