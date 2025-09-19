from django.contrib.auth.models import User
from .models import Category, Transaction
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, min_length = 6)
    class Meta:
        model = User
        fields = ("username", "password", "email")

    def create(self, validated_data):
        user = User(username=validated_data['username'], email=validated_data.get('email',''))
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "is_default")

class TransactionSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source = 'category.name', read_only = True)
    class Meta:
        model = Transaction
        fields = ("id", "type", "amount", "note", "date", "category", "category_name")
        

