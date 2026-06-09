from django.shortcuts import render
from django.http import HttpResponse 
from .models import MeinXOEVStandard

# Create your views here.
def home(request): 
    return HttpResponse("Hallo, meine kleine Django App läuft hier!")

def meinXoevStandard_list(request):
    daten = MeinXOEVStandard.objects.all().order_by("lieferant")
    return render(request, "meinxoevstandard_list.html", {"daten": daten})

def meinXoevStandard_list_kern(request):
    daten = MeinXOEVStandard.objects.all().order_by("lieferant")
    return render(request, "meinxoevstandard_list_kern.html", {"daten": daten})
