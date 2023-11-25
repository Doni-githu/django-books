from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer, UserSerializer
from . import models

class BookView(ModelViewSet):
    serializer_class = BookSerializer
    def get_queryset(self):
        return models.Book.objects.all()
    