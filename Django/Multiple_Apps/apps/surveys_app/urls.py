from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$', views.create),
url(r'^new', views.add)
]
