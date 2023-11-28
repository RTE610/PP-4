from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
path('',views.test),
    path('api/v1/hello-world14',views.Task)
]
