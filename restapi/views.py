from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from models import Author
from serilaizers import Authorserilaizers
# Create your views here.

class Authorview(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = Authorserilaizers
