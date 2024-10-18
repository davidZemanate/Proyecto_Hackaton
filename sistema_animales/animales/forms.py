from django import forms
from .models import Animal, Ayuda_Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nombre', 'edad', 'tipo',
                  'municipio','departamento',
                  'direccion','tipo_vulnerabilidad',
                  'ayuda_requerida','descripcion']

class AyudaForm(forms.ModelForm):
    class Meta:
        model = Ayuda_Animal
        fields = ['animal', 'descripcion']
