from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r'blog/(page-(\d+)/)?$', views.blog_articles),
    re_path(r'comments/(?:page-(?P<page_number>\d+)/)?$', views.comments),
    re_path(r'^blog/(?P<year>[0-9]{4})/$', views.optional_args, {'foo':'bar'}),
]

