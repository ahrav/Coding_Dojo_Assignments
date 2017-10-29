from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$', views.index),
url(r'^process/(?P<building_id>\d+)', views.process),
url(r'^reset$', views.reset)
]
