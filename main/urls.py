from django.contrib import admin
from django.urls import path, include  # Добавь include сюда

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('phones.urls')),  # Подключаем urls приложения phones
]