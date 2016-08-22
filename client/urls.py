from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.search, name="search"),
    url(r'^detail/(?P<venue_id>[a-zA-Z0-9]+)/$', views.venue_detail, name="venue_detail"),
]