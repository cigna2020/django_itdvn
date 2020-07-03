from django.shortcuts import render, redirect
from django.http import HttpResponse

def hello_response(request):
    return HttpResponse('Hello Django response!')

def http_redirect(request):
    return redirect('/lesson-two-response/fun1/')

def fun1(request):
    return HttpResponse('Hello redirect!')

def render_html(requst):
    _html = """
            <html>
        <head><title>TITLE</title>
            <body>
                <h1>HELLO HTML!</h1>
            </body>
        </html>
    """
    return HttpResponse(_html)


def render_template(request):
    return render(request, "main.html", {})

def func_render_to_response(request):
    return render(request, 'main_render.html', {})

def form_hendler(request):
    if request.method == 'POST':
        return HttpResponse('Request is POST')
    else:
        return HttpResponse('Request is GET')