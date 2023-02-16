from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import Author
from .serializers import Authorserilaizers
# Create your views here.

# class Authorview(ModelViewSet):
#     queryset = Author.objects.all()
#     serializer_class = Authorserilaizers

class AuthorListview(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = Authorserilaizers
    
class AuthorListCreateview(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = Authorserilaizers

class AuthorCreateview(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = Authorserilaizers

class AuthorDestroyview(generics.DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = Authorserilaizers

class AuthorRetrievedestroyview(generics.RetrieveDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = Authorserilaizers    