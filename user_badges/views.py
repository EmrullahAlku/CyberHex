from django.shortcuts import render
from .models import Badge

def badge_list(request):
    badges = Badge.objects.all()
    return render(request, 'user_badges/badge_list.html', {'badges': badges})

def badges_index(request):
    return render(request, 'user_badges/badges_index.html')