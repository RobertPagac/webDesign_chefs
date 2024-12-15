from rest_framework import serializers
from . models import *

# Users
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'password']

# Recipes
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    image = serializers.ImageField(required=False)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'secondary_description', 'ingredients', 'image']

# Event(s)
class EventSerializer(serializers.ModelSerializer):
    recipe = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all())

    class Meta:
        model = Event
        fields = [
            'id', 'date', 'max_attendees', 
            'registered_attendees', 'time_range', 
            'price', 'recipe'
        ]

class EventDetailSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer(read_only=True)
    joined_users = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True
    )

    class Meta:
        model = Event
        fields = [
            'id', 'date', 'max_attendees', 
            'registered_attendees', 'time_range', 
            'price', 'recipe', 'joined_users'
        ]