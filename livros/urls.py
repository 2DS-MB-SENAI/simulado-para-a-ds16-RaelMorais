from django.urls import path
from . import views  
from .views import *


urlpatterns = [
    path('livro/', view=views.get_livros),
    path('autores/', view=views.get_autores), 
    path('livros/<int:pk>', view=views.get_livros_id),
    path('autores/<int:pk', view=views.get_autores_id),
    path('autores/create', view=views.post_autores),
    path('livros/create', view=views.post_livros),
    path('livros/listar', view=views.listar_livros),
    path('autores/listar', view=views.listar_autores), 
]
