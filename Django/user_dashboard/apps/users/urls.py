from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$', views.index),
url(r'^signin$', views.signin),
url(r'^register$', views.register),
url(r'^login$', views.login),
url(r'^login_success', views.login_success),
url(r'dashboard$', views.dashboard),
url(r'dashboard/admin', views.admin_dashboard),
url(r'users/show/(?P<user_id>\d+)', views.show),
url(r'delete/(?P<user_id>\d+)', views.delete),
url(r'users/edit/(?P<user_id>\d+)', views.edit_user),
url(r'edit_info/(?P<user_id>\d+)', views.edit_info),
url(r'users/edit$', views.edit_self),
url(r'update_password/(?P<user_id>\d+)', views.update_password)
]
