from django.conf.urls import url
from . import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.date_list, name='date_list'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^dateideas/$', views.idea_list),
    url(r'^dateideas/(?P<pk>[0-9]+)/$', views.idea_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
