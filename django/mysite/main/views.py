from django.http import HttpResponse
from django.shortcuts import render


#здесь отображается видимое избражение в браузере

def main_viev(request):
    return HttpResponse('This my site'
                        'fucking shit')