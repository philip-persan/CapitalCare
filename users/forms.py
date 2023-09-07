from django import forms
from django.core.exceptions import ValidationError

from .models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )


class UserForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(),
        label='Senha'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label='Confirmação de senha'
    )

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name',
            'email', 'phone', 'password1', 'password2'
        ]
        labels = {
            'username': 'Nome de usuário',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'phone': 'Telefone',
        }

        def clean_email(self):
            email = self.cleaned_data['email']
            exists = User.objects.filter(email=email).exists()

            if exists:
                raise forms.ValidationError(
                    'Este email já existe', code='invalid',
                )

            return email

        def clean_username(self):
            username = self.cleaned_data['username']
            exists = User.objects.filter(email=username).exists()

            if exists:
                raise forms.ValidationError(
                    'Este usuário já existe', code='invalid',
                )

            return username

        def clean(self):
            cleaned_data = super().clean()

            password = cleaned_data['password1']
            password2 = cleaned_data['password2']

            if password != password2:
                password_confirmation_error = ValidationError(
                    'Password1 and password2 must be equal',
                    code='invalid'
                )
                raise ValidationError({
                    'password': password_confirmation_error,
                    'password2': [
                        password_confirmation_error,
                    ],
                })
