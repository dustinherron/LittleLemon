#define URL route for index() view
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('restaurant/menu/', views.MenuItemView.as_view()),
    path('restaurant/menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('restaurant/', views.index, name='index'),

]