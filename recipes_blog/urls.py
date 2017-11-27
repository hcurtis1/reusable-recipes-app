from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.post_lists),
    url(r'^(?P<id>\d+)/$', views.post_detail),
]
