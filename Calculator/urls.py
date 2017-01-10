from django.conf.urls import url
from . import views

app_name = "Calculator"

urlpatterns = [
    url(r'^(?P<client>[0-2])/$', views.index, name='index'),
    url(r'^register$', views.user_register, name='register'),
    url(r'^$', views.user_login, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^accept$', views.user_accept, name='accept'),
    url(r'^type$', views.user_type, name='type'),
    url(r'^chart$', views.user_chart, name='chart'),
               #url(r'^(?P<id>[0-9]+)/$', , name='detail'),
               
               # url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]
