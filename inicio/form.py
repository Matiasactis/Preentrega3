from django import forms

class CrearPersonaFormulario(forms.Form):
    nombre= forms.CharField(max_length=20)
    edad = forms.IntegerField()
    
class CrearGatoFormulario(forms.Form):
    nombre= forms.CharField(max_length=20)
    edad = forms.IntegerField()

# class CrearPajaroFormulario(forms.Form):
#     nombre= forms.CharField(max_length=20)
#     edad = forms.IntegerField()
#     color =forms.CharField(required=False)