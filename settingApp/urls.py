from django.urls import path
from .views import affichage_, DetailCasier, downloadfile, downloadpreview_, about_us

app_name = "settingApp"

urlpatterns = [
    path("", affichage_, name="affichage"),
    path("detail/<int:pk>", DetailCasier.as_view(), name="detail"),
    path("detail/<int:pk>/download", downloadfile, name="downloadfile"),
    path("telecharger/extrait/", downloadpreview_, name="downloadfilepreview"),
    path("apropos", about_us, name="auteur"),

]
