from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from .models import Booking, Menu
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.response import Response
# Create your views here.

def sayHello(request):
    return HttpResponse("Hello World")

def index(request):
    return render(request,'index.html',{})

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItem(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer