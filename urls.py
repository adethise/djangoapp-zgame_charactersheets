from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name = 'index'),
        url(r'^create$', views.create, name = 'create'),
        url(r'^view/(?P<character_id>[0-9]+)$', views.view, name = 'view')
]
