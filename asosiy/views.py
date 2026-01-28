from django.shortcuts import render, get_object_or_404

from .models import Main_Movie, Purchase_Movie, IshTuri, AsosiyIsh

def base(request):
    return render(request, "base.html")




def navigation(request):
    return render(request, "navigation.html")

def footer(request):
    return render(request, "footer.html")


def home(request):
    kino = Main_Movie.objects.all()
    return render(request, "home.html", {"kino": kino})
def movi_inside(request, movie_id):
    kino = get_object_or_404(Main_Movie, id=(movie_id))
    return render(request, "movi_inside.html", {"kino": kino})


def aloqa(request):
    return render(request, "aloqa.html")


def qoida(request):
    return render(request, "qoida.html")

def premyera(request):
    kino_purchase = Purchase_Movie.objects.all()
    return render(request, "premyera.html", {"kino_purchase": kino_purchase})


def work(request):
    ishlar = AsosiyIsh.objects.filter(ish_turi__ish_turi="Shifokor")
    return render(request, "ish.html", {"ishlar": ishlar})
    
def work_second(request):
    ishlar = AsosiyIsh.objects.filter(ish_turi__ish_turi="Usta")
    return render(request, "ish_second.html", {"ishlar": ishlar})

# movie_id == id
# id == 1
# id  == 2
# id == 3
# Main_Movie


# relative
# models
# get_object_or_404