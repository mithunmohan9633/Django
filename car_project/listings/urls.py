from django.urls import path, include  
from . import views
from .views import CarForSaleView,AddCarView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', views.user_registration, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('cars/', CarForSaleView.as_view(), name='car_list'),
    path('cars/add/', AddCarView.as_view(), name='add_car'),
]

