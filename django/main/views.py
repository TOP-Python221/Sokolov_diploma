from django.shortcuts import render
from django.shortcuts import HttpResponse

def home_view(request):
    return render(request, 'index.html')
