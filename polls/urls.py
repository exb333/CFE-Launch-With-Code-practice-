from django.conf.urls import url
from polls import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^(?P<ref_id>.*)$', views.share, name='share'),

]