from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^users/create$', views.create),
    url(r'^users/(?P<id>\w+)$', views.show), 
    url(r'^users/(?P<id>\w+)/edit$', views.update), 
    url(r'^users/(?P<id>\w+)/destroy$', views.destroy)
]