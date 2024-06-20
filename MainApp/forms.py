from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm,UserCreationForm
from .models import Avatar


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. Ingrese una dirección de correo electrónico válida.")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class EditUserPasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['new_password1', 'new_password2']:
            self.fields[field_name].required = False

    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        if new_password1 and new_password2:
            if new_password1 != new_password2:
                raise forms.ValidationError(
                    "Las contraseñas no coinciden."
                )

        return cleaned_data
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields=('imagen',)