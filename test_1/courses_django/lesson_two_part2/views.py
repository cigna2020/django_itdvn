from django.shortcuts import render
from django.http import HttpResponse


def blog_articles(request, a, b):
    return HttpResponse("bloq articles, %s, %s" %(a, b))

def comments(request, page_number):
    return HttpResponse('comments, %s' %page_number)

def optional_args(request, year, foo):
    return HttpResponse('optional_args %s' % foo)

def history(request, page_slug, page_id):
    return HttpResponse("history")

def edit(request, page_slug, page_id):
    return HttpResponse("edit")

def discuss(request, page_slug, page_id):
    return HttpResponse("discuss")

def permissions(request, page_slug, page_id):
    return HttpResponse("permissions")


