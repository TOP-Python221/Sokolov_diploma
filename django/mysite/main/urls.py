from django.urls import path
from main import views


urlpatterns = [
    path('',views.main_viev), # проверяет адрес на пустую строку и проверяет следующий адрес,
    path('about',views.about_view), #подключили еще одну страницу и указали для нее путь
    path('cake_builder',views.cake_builder),
]