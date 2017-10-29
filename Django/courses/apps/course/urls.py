from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$', views.index),
url(r'^courses/delete/(?P<id>\d+)', views.delete),
url(r'^add_course', views.add)
]
