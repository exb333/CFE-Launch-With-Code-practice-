from django.conf.urls import url
from polls import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	# url(r'^home2/$', views.home2, name='home2'),

]