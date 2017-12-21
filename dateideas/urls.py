from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.date_list, name='date_list'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
]
