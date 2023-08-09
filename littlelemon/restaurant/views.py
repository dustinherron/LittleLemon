
# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import Menu
from .serializers import MenuItemSerializer

# Create your views here. 
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer