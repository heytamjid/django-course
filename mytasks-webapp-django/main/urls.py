from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("alltasks", views.alltasks, name = "alltasks"),
    path("completedtasks", views.completedtasks, name = "completedtasks"),
    path("add/", views.add, name = "add"),
    path("addbackend/", views.addbackend, name = "addbackend"),
    path("/edit/<int:task_id>/", views.edit, name = "edit"),
    path("/complete/<int:task_id>/", views.complete, name = "complete"),
    path("/delete/<int:task_id>/", views.delete, name = "delete"),
    path("/deletecompleted/<int:task_id>/", views.deletecompleted, name = "deletecompleted"),
    path("/incompletecompleted/<int:task_id>/", views.incomplete, name = "incompleteit"),
    path("/editbackend/<int:task_id>/", views.editbackend, name = "editbackend"),
    path("/editbackendforcompleted/<int:task_id>/", views.editbackendforcompleted, name = "editbackendforcompleted"),
]
