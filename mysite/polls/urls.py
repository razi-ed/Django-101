from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^awesome/$',views.index,name='index'),
    url(r'^totally-cool/$', views.t_c, name="t_c")
    ]