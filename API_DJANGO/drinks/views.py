

from django.http import HttpResponse
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def index(request):
    return HttpResponse("THis is testing application of API and DOCKEr")


@api_view(['GET', 'POST'])
def drink_list(request, format=None):

    if request.method == 'GET':

        drinks = Drink.objects.all()
        serialize = DrinkSerializer(drinks, many = True)
        return  Response(serialize.data)

    if request.method == 'POST':
        
        serialize = DrinkSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
@api_view(['GET', 'PUT', 'DELETE'])
def drink_details(request, id, format=None):
    try:
        drink = Drink.objects.get(pk=id)

    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serialize = DrinkSerializer(drink)
        return Response(serialize.data)
    elif request.method == 'PUT':
        serialize = DrinkSerializer(drink, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
