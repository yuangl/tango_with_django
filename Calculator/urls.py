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
    url(r'^questionnaire/(?P<key>.+)/$', views.user_questionnaire, name='questionnaire'),
    url(r'^email_address$', views.user_email_address, name = 'email_address'),
    url(r'^reset_password/(?P<key>.+)/$', views.user_reset_password, name = 'reset_password'),
    url(r'^error$', views.user_error, name = 'user_error'),
    url(r'^webinar_menu$', views.webinar_menu, name = 'webinar_menu'),
    url(r'^home$', views.return_index, name='return_index'),
    url(r'^infor$', views.user_infor, name='user_infor'),
    url(r'^news$', views.economic_news, name='news'),
    url(r'^plan$', views.user_plan, name='plan'),
    
    #url(r'^webinar$', views.webinar, name = 'webinar'),
    
    #url(r'^questionnaire$', views.user_questionnaire, name='questionnaire'),
    
               #url(r'^(?P<id>[0-9]+)/$', , name='detail'),
               
               # url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]
