# Generated by Django 3.0.6 on 2020-05-12 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=30, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellido')),
                ('position', models.CharField(choices=[('Directivo', 'Directivo'), ('Asesor', 'Asesor'), ('Operativo', 'Operativo'), ('Tecnico', 'Tecnico'), ('Asistencial', 'Asistencial')], max_length=50)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.Departamento')),
            ],
        ),
    ]