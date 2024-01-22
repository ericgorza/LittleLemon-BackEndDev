from django.urls import path
from .views import sayHello, index, MenuItemView, SingleMenuItem
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('test', sayHello, name='sayHello'),
    path('', index, name='index'),
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>', SingleMenuItem.as_view()),
    path('api-token-auth/', obtain_auth_token),
]