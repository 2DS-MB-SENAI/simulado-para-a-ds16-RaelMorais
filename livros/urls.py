from django.urls import path
from . import views  
from .views import *


from django.urls import path
from . import views

urlpatterns = [
    # URL para listar livros
    path('livros/', view=views.get_livros, name='get_livros'),  # GET para listar livros
    # URL para criar um novo livro
    path('livros/', view=views.post_livros, name='post_livros'),  # POST para criar um livro
    
    # URL para acessar livros por ID
    path('livros/<int:pk>/', view=views.get_livros_id, name='get_livros_id'), 
    
    # URL para listar autores
    path('autores/', view=views.get_autores, name='get_autores'),  # GET para listar autores
    # URL para criar um novo autor
    path('autores/', view=views.post_autores, name='post_autores'),  # POST para criar um autor
    
    # URL para acessar autores por ID
    path('autores/<int:pk>/', view=views.get_autores_id, name='get_autores_id'), 
]
