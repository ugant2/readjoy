from django.conf.urls import url
from figure import views

app_name = 'figure'

urlpatterns = [
    url(r'^figure/', views.test_matplotlib, name='matplottest'),
    url(r'^figures/', views.circle_area, name='matplottests'),
]
