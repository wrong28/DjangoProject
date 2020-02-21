from django.conf.urls import url
from basicApp import views


#Template Tagging

app_name = 'basicApp'

urlpatterns = [
#	url(r'^$',views.index,name='index')
	url(r'^relative/$',views.relative,name='relative'),
	url(r'^other/$',views.other,name='other'),
]
