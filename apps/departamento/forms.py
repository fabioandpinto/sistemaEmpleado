from django import forms

# model


types = (
    ('O', 'Operativo'),
    ('A', 'Administrativo'),
)


class NewDepartmentForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    department = forms.CharField(max_length=50)
    short_name = forms.CharField(max_length=50)
    type = forms.ChoiceField(choices=types)
    is_active = forms.BooleanField()
