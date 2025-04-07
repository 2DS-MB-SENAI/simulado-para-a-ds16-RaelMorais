from django.urls import path
from . import views  
from .views import *


urlpatterns = [
    path('logar/', view=views.create_user),
    path('registro/', view=views.login_user, name='Login User'),
    path('read/', view=views.root, name="Read Data"),

]