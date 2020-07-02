from django.urls import path, re_path
from . import views

urlpatterns = [
    path(r'', views.home),
    path(r'items', views.items, name='items'),
    path(r'item/2003/', views.special_case_2003, name = 'special_case_2003'),
    re_path(r'^item/(?P<year>[0-9]{4,5})/$', views.year_archive, name='year_archive'),
    re_path(r'^item/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})$', views.month_archive, name = 'month_archive'),
    re_path(r'^item/(?P<year>[\d]{4})/(?P<month>[0-9]{2})/(?P<day>[\d]{2})/$', views.day_archive, name = 'day_archive'),
    re_path(r'book/page$', views.page, name='page'),
    re_path(r'^book/page(?P<num>[0-9]+)$', views.page, name='page'),
    # path(r'^item/?P<year>[\w]+)$', views.show_url_param, name = 'show_url_param'),
]