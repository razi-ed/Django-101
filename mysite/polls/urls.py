from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^totally-cool/$', views.t_c, name="t_c"),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.result, name='result'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name="vote")
    ]