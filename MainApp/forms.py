from django import forms

class miRegistro(forms.Form):
    nombre = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
