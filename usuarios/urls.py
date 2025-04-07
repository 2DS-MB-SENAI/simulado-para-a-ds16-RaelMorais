from django.urls import path
from . import views  
from .views import *


urlpatterns = [
    path('registro/', view=views.create_user),
    path('login/', view=views.login_user),
    path('read/', view=views.root, name="Read Data"),

]