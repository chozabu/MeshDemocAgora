 
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /agora/
    url(r'^$', views.index, name='index'),
    # ex: /agora/new_user/
    url(r'^new_user/$', views.new_user, name='new_user'),
    # ex: /agora/login/
    url(r'^login/$', views.login_user, name='login'),
    # ex: /agora/logout/
    url(r'^logout/$', views.logout_user, name='logout'),
    # ex: /agora/topics/
    url(r'^topics/$', views.topics, name='topics'),
    # ex: /agora/topics/5/
    url(r'^topics/(?P<topic_id>[0-9]+)/$', views.topics, name='topics'),
    # ex: /agora/topics/new/
    url(r'^topics/new/$', views.new_topic, name='newtopic'),
    # ex: /agora/topics/new/
    url(r'^topics/new/(?P<parent_topic_id>[0-9]+)/$', views.new_topic, name='newtopic'),
    # ex: /agora/topics/5/newrep/
    url(r'^topics/(?P<parent_topic_id>[0-9]+)/newrep$', views.new_rep, name='newrep'),
    # ex: /agora/topics/new/
    url(r'^topics/(?P<parent_topic_id>[0-9]+)/newpost/$', views.new_post, name='newpost'),
    # ex: /agora/topics/new/
    url(r'^topics/(?P<parent_topic_id>[0-9]+)/newpost/(?P<parent_post_id>[0-9]+)$', views.new_post, name='newpost'),
    # ex: /agora/topics/5/posts/5/
    url(r'^topics/(?P<topic_id>[0-9]+)/posts/(?P<post_id>[0-9]+)$', views.posts, name='posts'),
    # ex: /agora/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]