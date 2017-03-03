from django.conf.urls import url
from polls import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
]