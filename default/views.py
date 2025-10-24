from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django import forms
from users.models import User
from .forms import StyledSignupForm

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "pages/home.html"

class PerfilView(LoginRequiredMixin, TemplateView):
    template_name = "pages/perfil.html"

class CuotasView(LoginRequiredMixin, TemplateView):
    template_name = "pages/cuotas.html"

class OnlyAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin_staff()

class AdminDashboardView(LoginRequiredMixin, OnlyAdminMixin, TemplateView):
    template_name = "pages/admin_dashboard.html"

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.role = User.Roles.STUDENT
        if commit:
            user.save()
        return user

class SignupView(CreateView):
    template_name = "auth/signup.html"
    form_class = StyledSignupForm
    success_url = reverse_lazy("login")
