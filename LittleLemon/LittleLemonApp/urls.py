from django.urls import path
from .views import sayHello, index

urlpatterns = [
    path('test', sayHello, name='sayHello'),
    path('', index, name='index'),
]