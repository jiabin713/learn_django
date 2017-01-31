from django.conf.urls import url

from polls import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<quesiton_id>[0-9]+)/$', views.detail, name='detil'),
    url(r'^(?P<quesiton_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<quesiton_id>[0-9]+)/vote/$', views.vote, name='vote'),

]