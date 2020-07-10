from django.conf.urls import url, include, re_path
from django.contrib import admin
# from lesson_two import views
from django.conf.urls.static import static
from .views import List


urlpatterns = [
    url(r'^$', List.as_view(), name='list-view'),
]