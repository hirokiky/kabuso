from django.conf.urls import patterns, url

from webfront import views

urlpatterns = patterns(
    '',
    url(r'^read/$', views.read_page, name='read_page'),
    url(r'^page/(?P<page_id>\d+)$', views.page_detail, name='page_detail'),
)