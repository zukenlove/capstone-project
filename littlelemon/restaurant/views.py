from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from .models import Menu, Booking
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

# # Create your views here.
def index(request):
    return render(request,'restaurant/index.html', {})
    
class MenuViewset(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = []
        else :
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
class UserViewset(viewsets.ModelViewSet):
    queryset =  User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = []
        else :
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
     
    
    # setup the booking view class
class BookingViewset(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]