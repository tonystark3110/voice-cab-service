from django.conf.urls import url, include
from . import views

app_name = 'homepage'

urlpatterns = [
    url(r'^$', views.menu_view, name="menu"),
    url(r'^login$', views.login_view, name="login"),
    url(r'^compose/$', views.compose_view, name="compose"),
    url(r'^inbox/$', views.inbox_view, name="inbox"),
    url(r'^sent/$', views.sent_view, name="sent"),
    url(r'^trash/$', views.trash_view, name="trash"),
    url(r'^search/$', views.search_view, name="search"),
    url(r'^map/$', views.map_view, name="map"),
    url(r'^direction/$', views.direction_view, name="direction"),
    url(r'^options/$', views.options_view, name="options"),
    url(r'^taxi/$', views.taxi_view, name="taxi")
]
