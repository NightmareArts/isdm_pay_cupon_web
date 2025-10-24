from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from default import views as dv
from default.forms import (
    StyledAuthenticationForm,
    StyledPasswordResetForm,
    StyledSetPasswordForm,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("login/", auth_views.LoginView.as_view(
        template_name="auth/login.html",
        authentication_form=StyledAuthenticationForm
    ), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    path("signup/", dv.SignupView.as_view(), name="signup"),

    path("password-reset/", auth_views.PasswordResetView.as_view(
        template_name="auth/password_reset.html",
        form_class=StyledPasswordResetForm
    ), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name="auth/password_reset_done.html"
    ), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="auth/password_reset_confirm.html",
        form_class=StyledSetPasswordForm
    ), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(
        template_name="auth/password_reset_complete.html"
    ), name="password_reset_complete"),

    path("", dv.HomeView.as_view(), name="home"),
    path("perfil/", dv.PerfilView.as_view(), name="perfil"),
    path("cuotas/", dv.CuotasView.as_view(), name="cuotas"),
    path("admin-panel/", dv.AdminDashboardView.as_view(), name="admin_panel"),
]
