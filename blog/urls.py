from django.conf.urls import url

from . import views

app_name = 'posts'
urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='home'),
    url(r'^posts/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='detail'),
]
