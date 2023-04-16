from django.apps import AppConfig

#на этот класс ссылаемся приподключении приложений, так же его нужно подключить в
#настройках
class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
