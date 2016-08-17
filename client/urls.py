from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.search_place, name='search_place'),
    url(r'^mahmut/', views.mahmut, name="mahmut"),


]