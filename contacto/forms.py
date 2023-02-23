from django import forms

class ContactoForm(forms.Form):

    nombre = forms.CharField(max_length=300, required=True)
    email = forms.EmailField(max_length=400, required=True)
    contenido = forms.CharField(max_length=3000, required=True)