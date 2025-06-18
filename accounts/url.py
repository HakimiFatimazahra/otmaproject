
from django.urls import path
from . import views  # ici . = accounts
from django.contrib.auth import views as auth_views
from omtaapp import views




urlpatterns = [

    path('signup/', views.signup, name='signup'),
    path('page/', views.pageentre, name='pageentre'),
    path('home/', views.htmlfile_view, name='htmlfile'),
    
    #path("login/", views.login, name="login"),
   
]
