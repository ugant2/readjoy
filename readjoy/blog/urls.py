from django.conf.urls import url, include
from blog import views

app_name = 'blogs'

urlpatterns = [
    url(r'^$', views.HomeListView.as_view(), name='home_pg'),
    url(r'^about/', views.AboutListView.as_view(), name='about_pg'),
    url(r'^accounts/', include('django.contrib.auth.urls'), name='login'),  # /accounts/login/ is a default for login
    url(r'^new_register/', views.register, name='register'),
    url(r'^new_post/', views.new_post, name='post_pg'),
    url(r'^contact/', views.contact_form, name='contact_pg'),
    url(r'apidoc/', views.api_doc, name='api_doc'),
    url(r'^api/posts/', views.post_list_api, name='list_api_view'),
    url(r'^api/post/(?P<pk>[0-9]+)/$', views.post_detail_api, name='detail_api_view'),
    url(r'^blogapi/', include('blog.api.urls'), name='blogapi'),
    url(r'^profile/', views.UserProfleListView.as_view(), name='profile_pg'),
    url(r'^detail/(?P<pk>\d+)', views.PostDetailView.as_view(), name='detail_pg'),
]
