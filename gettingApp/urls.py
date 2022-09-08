from django.urls import path
from .views import home, searchbyname, searchByImage

app_name = "gettingApp"

urlpatterns = [
    path('', home, name="gettingApp_home"),
    path('search/', searchbyname, name="gettingApp_searchbyname"),
    path('search/byimg/', searchByImage, name='gettingApp_seacrchbyImage'),
]

