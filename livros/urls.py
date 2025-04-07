from django.urls import path
from . import views  
from .views import *


urlpatterns = [
    path('livros/', view=views.get_livros),
    path('autores/', view=views.get_autores), 
    
    path('livros/<int:pk>', view=views.get_livros_id),
    path('autores/<int:pk', view=views.get_autores_id),

    path('autores/', view=views.post_autores),
    path('livros/', view=views.post_livros),

    path('livros/', view=views.listar_livros),
    path('autores/', view=views.listar_autores), 
]
