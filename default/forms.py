from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm, PasswordResetForm, SetPasswordForm
)
from users.models import User

# Login
class StyledAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Nombre de usuario",
            "id": "id_username"
        })
        self.fields["password"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Contraseña",
            "id": "id_password"
        })

# Registro (para tu CustomUser)
class StyledSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")  # rol = STUDENT por defecto en model
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "class": "form-control", "placeholder": "Usuario"
        })
        self.fields["email"].widget.attrs.update({
            "class": "form-control", "placeholder": "correo@ejemplo.com"
        })
        self.fields["password1"].widget.attrs.update({
            "class": "form-control", "placeholder": "Contraseña"
        })
        self.fields["password2"].widget.attrs.update({
            "class": "form-control", "placeholder": "Repetir contraseña"
        })

# Reset (solicitud por email)
class StyledPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({
            "class": "form-control", "placeholder": "correo@ejemplo.com"
        })

# Confirmar nueva contraseña (desde enlace)
class StyledSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["new_password1"].widget.attrs.update({
            "class": "form-control", "placeholder": "Nueva contraseña"
        })
        self.fields["new_password2"].widget.attrs.update({
            "class": "form-control", "placeholder": "Repetir nueva contraseña"
        })
