

from django.conf.urls import url

from . import views


app_name = 'myaccount'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new_visit/$', views.new_visit, name='new_visit'),
    url(r'^add_visit/$', views.add_visit, name='add_visit'),
    url(r'^edit_entry/$', views.edit_entry, name='edit_entry'),
    url(r'^make_entry/$', views.make_entry, name='make_entry'),
    url(r'^show_entry/$', views.show_entry, name='show_entry'),
]