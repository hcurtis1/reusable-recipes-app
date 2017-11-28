from django.conf.urls import url
from recipes_blog import views

urlpatterns = [
    url(r'^$', views.post_lists),
    url(r'^(?P<id>\d+)/$', views.post_detail),
]
