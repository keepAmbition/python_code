from django.conf.urls import url
from app import views
urlpatterns = [
    url(r'^host$', views.host),
    url(r'^test_ajax$', views.test_ajax),
    url(r'^edit$', views.edit),
    url(r'^del$', views.delete),
    url(r'^app$', views.app),
    url(r'^ajax_add_app$', views.ajax_add_app),
    url(r'^ajax_submit_edit$', views.ajax_submit_edit),
    url(r'^ajax_submit_delete$', views.ajax_submit_delete),
    url(r'^host_detail$', views.host_detail),
]
