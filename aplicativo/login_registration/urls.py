from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="landing"),
	url(r'^register$', views.register, name="register"),
	url(r'^login$', views.login, name="login"),
	url(r'^logout$', views.logout, name="logout"),
	# url(r'^success$', views.success, name="dashboard"),

	# Another aplicativo to defined a dashboard route
]