""" Form for register person"""

from django import forms
from .models import Empleado

# Model Form
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ('__all__')

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese texto aquí'
                }
            )
        }

    def clean_first_name(self):
        nombre = self.cleaned_data['first_name']
        if nombre == 'Jorge':
            raise forms.ValidationError('No se puede colocar ese nombre')
        return nombre