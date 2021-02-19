from django.conf.urls import include, url
from django.contrib import admin
from training import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.training_index),
]


