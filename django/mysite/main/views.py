from django.http import HttpResponse
from django.shortcuts import render


#здесь отображается видимое избражение в браузере

def main_viev(request):
    return HttpResponse('<h1>This my site\n<h1>'
                        '<p>fucking shit<p>')


def about_view(request):
    #   передаем объект request и отностельный путь до страницы
    return render(request, 'main/about.html')