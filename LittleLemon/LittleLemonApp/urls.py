from django.urls import path
from .views import sayHello, index, MenuItemView, SingleMenuItem

urlpatterns = [
    path('test', sayHello, name='sayHello'),
    path('', index, name='index'),
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>', SingleMenuItem.as_view()),
]