from django.urls import path, re_path, include
from . import views


urlpatterns = [
    re_path(r'^$', views.hello_response),
    re_path(r'^redirect/$', views.http_redirect),
    re_path(r'^fun1/$', views.fun1),
    re_path(r'^render-html/$', views.render_html),
    re_path(r'^render-template/$', views.render_template),
    re_path(r'^render-to-response/$', views.func_render_to_response),
    re_path(r'render-template/form-hendler/$', views.form_hendler),
]