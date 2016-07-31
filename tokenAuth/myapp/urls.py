from django.conf.urls import patterns, url
from . import views

urlpatterns = [
url(r'^tasks/$', views.user_list, name='user_list'),
url(r'^token/(?P<pk>[0-9]+)$', views.user_detail, name='user_detail'),
url(r'^payload/(?P<pk>[0-9]+)$', views.get_payload, name='get_payload'),

]
