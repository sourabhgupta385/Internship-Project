from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^/bollywood/$', views.bollywood, name='bollywood'),
    url(r'^/business/$', views.business, name='business'),
    url(r'^/education/$', views.education, name='education'),
    url(r'^/entertainment/$', views.entertainment, name='entertainment'),
    url(r'^/health/$', views.health, name='health'),
    url(r'^/india/$', views.india, name='india'),
    url(r'^/lifestyle/$', views.lifestyle, name='lifestyle'),
    url(r'^/realstate/$', views.realstate, name='realstate'),
    url(r'^/sports/$', views.sports, name='sports'),
    url(r'^/technology/$', views.technology, name='technology'),
    url(r'^/world/$', views.world, name='world'),
]
