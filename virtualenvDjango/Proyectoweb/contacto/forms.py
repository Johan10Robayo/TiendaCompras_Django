from django import forms

class Formulario_contacto(forms.Form):
    nombre=forms.CharField(label="nombre",required=True)
    email=forms.CharField(label="email",required=True)
    contenido=forms.CharField(widget=forms.Textarea)