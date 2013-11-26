from django.conf.urls import patterns, url
from dairy_farm import views

urlpatterns = patterns('',
	url(r'^home/$', views.app_main, name='app_main'),

	url(r'^(?P<table>\w+)/create/$',views.create, name='create'),
	url(r'^save/$', views.save, name='save'),
)