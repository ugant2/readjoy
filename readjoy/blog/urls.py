

from django.conf.urls import url
from blog import views

app_name = 'blogs'

urlpatterns = [
    url(r'^$', views.HomeListView.as_view(), name='home_pg'),
    url(r'^about/', views.AboutListView.as_view(), name='about_pg'),
    url(r'^detail/(?P<pk>\d+)', views.PostDetailView.as_view(), name='detail_pg'),
]
