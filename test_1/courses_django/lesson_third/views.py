from django.shortcuts import render
import datetime, math
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def view(request):
    list = [0, 232, 45, 123, 4, 53423, 54, 23]
    template = loader.get_template('index.html')
    context = {
        'test': 'TEXT!',
        'list': list,
        'name': 'Alex',
        'surname': 'Jezus',
        'coords': {
            'x': 'x coords',
            'y': 'y coords',
        },
        'list': [1, 2, 3, 4]
    }
    return HttpResponse(template.render(context, request))
