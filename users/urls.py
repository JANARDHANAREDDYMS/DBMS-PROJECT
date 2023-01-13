from django.urls import path

from . import views


urlpatterns =[
    path("",views.index,name="index"),
    path("login",views.usr_login,name="usr_login"),
    path("logout",views.usr_logout,name="usr_logout")
]