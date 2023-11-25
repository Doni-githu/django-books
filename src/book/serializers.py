from rest_framework import serializers
from .models import Book, User  


class BaseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

class BookSerializer(BaseSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class UserSerializer(BaseSerializer):
    class Meta:
        model = User
        fields = "__all__"