from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from .models import Menu, Booking
from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

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
    
    
class MenuSerializerView(APIView):
    def get(self, request):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class MenuViewset(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class UserViewset(viewsets.ModelViewSet):
    queryset =  User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = []
        else :
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
            
    # permission_classes = [IsAuthenticated]
    # Override the GET for list view (GET /users/)
    def list(self, request, *args, **kwargs):
        users = self.get_queryset()
        serializer = self.get_serializer(users, many=True)
        return Response({
            "count": users.count(),
            "users": serializer.data
        })
        
    # Override the GET for a Single User
    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response({
            "user_details": serializer.data,
            "message": "Here’s your user!"
        })

        
    
    # setup the booking view class
class BookingViewset(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]