from django.conf.urls import url, include
from django.urls import path, re_path
from . import views


urlpatterns = [
    url(r'^filters$', views.filter),
    re_path(r'^view/$', views.view),
    url(r'^tags-if/$', views.tags_if),
    url(r'^tags-for/$', views.tags_for),
    url(r'^regroup/$', views.tag_regroup),
    url(r'^base/$', views.base),
    url(r'^adrian/$', views.adrian),
    url(r'^realese/$', views.realese),
    # url(r'^check/$', views.check),
    # url(r'^in/$', views.tag_in),
]