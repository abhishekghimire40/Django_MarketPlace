from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views
from .forms import LoginForm


app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("signup/", views.signup, name="signup"),
    # used django built in login view to handle login
    # NOTE: when logged in, it redirect to /accounts/profile so make sure to redirect it
    # to a path you want in settings.py file
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="core/login.html", authentication_form=LoginForm
        ),
        name="login",
    ),
]
