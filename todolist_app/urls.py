from django.urls import path
from todolist_app import views

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('contact', views.contact, name='Contact'),
    path('about', views.about, name='about'),
]
