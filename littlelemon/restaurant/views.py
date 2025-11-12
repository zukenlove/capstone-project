from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking

# Create your views here.
@api_view(['GET'])
def homeView(request):
    return Response({"message" : "My First API project"},status=status.HTTP_200_OK)


def index(request):
    return render(request, 'restaurant/index.html', {})


@api_view(["GET",'POST'])
def menuView(request):
    if request.method == "GET":
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == "POST":
        serializer = MenuSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    