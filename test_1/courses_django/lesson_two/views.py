from django.http import HttpResponse


def home(request):
    return HttpResponse('Home Page!')

def items(request):
    return HttpResponse("Welcome to localhost/items")

def special_case_2003(request):
    return HttpResponse("Welcome to localhost/item/2003!")

def year_archive(request, year):
    return HttpResponse("Welcome to localhost/[0-9]{4}! %s" %year)

def month_archive(request, year, month):
    return HttpResponse("Welcome to localhost/ %s// %s" %(year, month))

def day_archive(request, year, month, day):
    return HttpResponse("Welcome to localhost/ %s// %s -- %s" %(year, month, day))

def show_url_param(request):
    pass

def page(request, num = '1'):
    if num == '1':
        return HttpResponse('You have gone to the first page')
    else:
        return HttpResponse('You have gone to the page num %s!' % num)