from django.conf.urls import url
from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^form/$', views.UserCreate.as_view(), name='form'),
    url(r'^$', views.IndexView.as_view(), name='index'),
]
