from django.shortcuts import render
import datetime, math
from django.http import HttpResponse
from django.template import loader

# Create your views here.

# def view(request):
#     list = [0, 232, 45, 123, 4, 53423, 54, 23]
#     template = loader.get_template('index.html')  # УСТАРЕЛЛЫЙ ВАРИАНТ
#     context = {
#         'test': 'TEXT!',
#         'list': list,
#         'name': 'Alex',
#         'surname': 'Jezus',
#         'coords': {
#             'x': 'x coords',
#             'y': 'y coords',
#         },
#         # 'list': [1, 2, 3, 4]
#     }
#     return HttpResponse(template.render(context, request))

def view(request):
    list = [0, 232, 45, 123, 4, 53423, 54, 23]
    context = {
        'test': 'TEXT!',
        'list': list,
        'name': 'Alex',
        'surname': 'Jezus',
        'coords': {
            'x': 'x coords',
            'y': 'y coords',
        },
        # 'list': [1, 2, 3, 4]
    }
    return render(request, 'index.html', context)  # порядок (риквест, индекс...) важен!


def filter(request):
    array_for_sort = [
        {'name': 'zed', 'age': 19},
        {'name': 'emy', 'age': 22},
        {'name': 'joe', 'age': 31},
    ]
    context = {
        'name_low': 'LOWER',
        'value': 10,
        'first': [1, 2, 3, 4],
        'second': [5, 6, 7, 8],
        'str': "I'm using Django",
        'date': datetime.datetime.now(),
        'empty_one': '',
        'for_sort': array_for_sort,
        'float': 32.223,
        'number': 12345678,
        'boolean_var': True
    }
    return render(request, 'filter.html', context)