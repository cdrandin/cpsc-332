from django.conf.urls import patterns, url
from dairy_farm import views

urlpatterns = patterns('',
	url(r'^home/$', views.app_main, name='app_main'),

	#url(r'^herd/create/$', views.herd_create, name='herd_create'),
	#url(r'^herd/save/$', views.herd_save, name='herd_save'),

	url(r'^(?P<table>\w+)/create/$',views.create, name='create'),
	url(r'^save/$', views.save, name='save'),
)