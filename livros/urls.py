from django.urls import path
from . import views  
from .views import *


urlpatterns = [
    path('api/livros/', view=views.get_livros),
    path('livros/', view=views.get_livros),
    path('api/autores/', view=views.get_autores), 

    path('livros/<int:pk>', view=views.get_livros_id),
    path('autores/<int:pk', view=views.get_autores_id),

    path('api/autores/', view=views.post_autores),
    path('api/livros/', view=views.post_livros),

    path('api/livros/', view=views.listar_livro),
    path('autores/', view=views.listar_autores), 
]
