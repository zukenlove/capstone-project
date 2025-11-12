from rest_framework import serializers
from  .models import Booking, Menu
from django.contrib.auth.models import User


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id','title', 'price', 'inventory']
        
        
        
class BookingSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(source = 'booking_date')
    class Meta:
        model = Booking
        fields = ['id','name','no_of_guest','date']
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','groups']
