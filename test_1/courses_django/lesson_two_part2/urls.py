from django.urls import path, re_path, include
from . import views


# extra_patterns = [
#     re_path(r'^report/$', views.report),
#     re_path(r'^report/(?P<id>[0-9]+)/$', views.report),
# ]
#
#
# urlpatterns = [
#     re_path(r'blog/(page-(\d+)/)?$', views.blog_articles),
#     re_path(r'comments/(?:page-(?P<page_number>\d+)/)?$', views.comments),
#     re_path(r'^optional-args/(?P<year>[0-9]{4})/$', views.optional_args, {'foo':'bar'}),
#     re_path(r'extra/', include(extra_patterns)),
# ]

# urlpatterns = [
#     re_path(r'^(?P<page_slug>[\w]+)-(?P<page_id>[\w]+)/history/$', views.history),
#     path('<page_slug>-<page_id>/edit/', views.edit),
#     path('<page_slug>-<page_id>/discuss/', views.discuss),
#     path('<page_slug>-<page_id>/permissions/', views.permissions),
# ]

# the same as above but shorter
urlpatterns = [
    path('<page_slug>-<page_id>/', include([
        path('history/', views.history),
        path('edit/', views.edit),
        path('discuss/', views.discuss),
        path('permissions/', views.permissions),
    ])),
]