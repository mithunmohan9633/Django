from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import CustomUser
from django.views import View
from .models import CarForSale,CarForRent,OilType,Brand

def user_registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        my_location_link = request.POST.get('my_location_link')
        profile_picture = request.FILES.get('profilepick')  # Assuming profile picture is uploaded as a file
        whatsapp_number = request.POST.get('whatsapp_num')

        user = CustomUser(
            username=username,
            email=email,
            phone=phone,
            my_location_link=my_location_link,
            profile_picture=profile_picture,
            whatsapp_number=whatsapp_number
        )
        user.set_password(password)
        user.save()
        login(request, user)
        return redirect('home')

    return render(request, 'signup.html')
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'login.html')

    return render(request, 'login.html')
def home_view(request):
    return render(request, 'home.html')
def user_logout(request):
    logout(request)
    return redirect('home')
class CarForSaleView(View):
    def get(self, request):
        cars = CarForSale.objects.all()
        return render(request, 'car/car_list.html', {'cars': cars})
class AddCarView(View):
    def get(self, request):
        brands = Brand.objects.all()
        oils = OilType.objects.all()
        return render(request, 'car/add_car.html', {'brands': brands, 'oils': oils})
    def post(self, request):
        return redirect('car_list')  
