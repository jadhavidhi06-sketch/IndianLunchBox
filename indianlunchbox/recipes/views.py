from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Recipe
from .serializers import RecipeSerializer
import json


@api_view(['GET'])
def get_recipes(request):

    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def add_recipe(request):

    serializer = RecipeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def download_recipes(request):

    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def import_recipes(request):

    file = request.FILES['file']
    data = json.load(file)

    for recipe in data:
        Recipe.objects.create(
            title=recipe['title'],
            category=recipe['category'],
            description=recipe['description'],
            ingredients=recipe['ingredients'],
            instructions=recipe['instructions'],
            image=recipe['image']
        )

    return Response({"message": "Recipes Imported"})