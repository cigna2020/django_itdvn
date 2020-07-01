from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.show) # r - это регулярное выражение. "" - пустая строка (после 5650 или 8000 ничего нет). т.е. мы даем команду джанго, что когда он встретит "", то должен перейти к вью.шоу
]