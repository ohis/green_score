from django.conf.urls import url
#from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^main$', views.main),
    url(r'^company$', views.company),
    url(r'^user_score$', views.user_score),
    url(r'^profile/(?P<id>\d+)$', views.profile),
    #url(r'^profile$', views.profile),
    url(r'^login$', views.login),
    url(r'^register$', views.register)

    ]
