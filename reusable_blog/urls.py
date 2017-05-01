from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^/$', views.post_list, name='post_list'),
    url(r'^top5$', views.top5, name='top5'),
    url(r'^(?P<id>\d+)/$', views.post_detail),
    url(r'^(?P<id>\d+)/edit$', views.edit_post),

    url(r'^post/new/$', views.new_post, name='new_post'),
]
