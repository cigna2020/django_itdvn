from django.shortcuts import render
from django.http import HttpResponse   # ашттп ответ, метод, который говорит о том, что ответом будет строковым ответом
# Create your views here.


def show(request): # риквест - это запрос, который посылает пользователь на сервер джанго
    return HttpResponse('Hello Django and world!')

