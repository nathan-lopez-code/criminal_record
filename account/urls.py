from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView    # LogoutView
from .forms import LoginForm


app_name = "account"

urlpatterns = [
    path("login/", LoginView.as_view(template_name="account/login.html", authentication_form=LoginForm), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
