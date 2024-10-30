from django.urls import path, include  
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', views.user_registration, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]

