from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import LivrosSerializer, AutoresSerializer
from .models import Livro, Autores
from django.template import loader
from django.http import HttpResponse

# Get para trazer dados em geral. 
@api_view(['GET'])
def get_livros (request):
    livros = Livro.objects.all()
    serializer = LivrosSerializer(livros, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_autores (request):
    autores = Autores.objects.all()
    serializer = LivrosSerializer(autores, many=True)
    return Response(serializer.data)


# get para buscar por ID. 
@api_view(['GET'])
def get_livros_id(request, pk):
    try:
        livros = Livro.objects.get(pk=pk)
    except Livro.DoesNotExist:
        return Response({'Error': 'Livro não existe'}, status=status.HTTP_404_NOT_FOUND)
    serializer = LivrosSerializer(livros)
    return Response(serializer.data)

@api_view(['GET'])
def get_autores_id(request, pk):
    try:
        autor = Autores.objects.get(pk=pk)  # Corrigido para buscar um único autor
    except Autores.DoesNotExist:  # Corrigido para capturar a exceção correta
        return Response({'Error': 'Autor não existe'}, status=status.HTTP_404_NOT_FOUND)
    serializer = AutoresSerializer(autor)  # Corrigido para não usar 'many=True'
    return Response(serializer.data)

#Para renderizar no HTML 

def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros.html', {'livros':livros})

def listar_autores(request):
    autores = Autores.objects.all()
    return render(request, 'autores.html', {'autores':autores})


# Post para criação de livro
@api_view(['POST'])
def post_livros(request):
    if request.method == 'POST':
        serializer = LivrosSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Post para criação de autor
@api_view(['POST'])
def post_autores(request):
    if request.method == 'POST':
        serializer = AutoresSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
