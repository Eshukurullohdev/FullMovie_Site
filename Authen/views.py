from django.contrib.auth import authenticate, login as auth_login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import logging
logger = logging.getLogger(__name__)
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
    if request.method == "POST":
        username = request.POST.get("username", '').strip()
        password = request.POST.get("password", '').strip()
        
        if not username:
            logger.warning("Username bo'sh tekshirib qaytadan urubnub korin")
            messages.error(request, "Username bo'sh qolgan")
            return redirect("login")
        
        try:
            user = User.objects.get(username=username)
            if user.is_superuser:
                auth_login(request, user)
                logger.info("Admin tizimga kirdi")
                return redirect("home")
            else:
                if not password:
                    logger.warning({username}, "Parol bo'sh tekshirib qaytadan urunib korin")
                    return redirect("login")
                
                user = authenticate(username=username, password=password)
                if user:
                    auth_login(request, user)
                    messages.success(request, "Siz tzimga kirdingiz")
                    return redirect("home")
                else:
                    logger.warning({username},"login qilishda Nomalum xato")
                    return redirect("login")
        except User.DoesNotExist:
            logger.warning({username},"login qilishda  xato bor")
            return redirect("login") 
    return render(request, "login.html")


