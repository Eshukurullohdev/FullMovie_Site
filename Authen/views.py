from django.contrib.auth import authenticate, login as auth_login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirum_password = request.POST.get("parolni_tasdiqlash")
        
        if password != confirum_password:
            messages.error(request, "Parol mos emas")
            return redirect("register")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Bu email allaqochon royhatan otkan")
            return redirect(register)
        
        user = User.objects.create_user(email=email, username=username, password=password)
        user.save()
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            messages.success(request, "Siz Tizimga Kirdingiz")
            return redirect("home")
        
        messages.error(request, "Nomalum Xato")
        return redirect("register")
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")


