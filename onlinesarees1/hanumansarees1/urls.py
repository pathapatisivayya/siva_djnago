from django.contrib import admin
from django.urls import path

from django.conf.urls import url

from hanumansarees1 import views





urlpatterns = [
    url(r'', views.dataview),
]
