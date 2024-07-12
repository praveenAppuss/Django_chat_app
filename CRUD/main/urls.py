from django.urls import path
from .import views

urlpatterns =[
    path('',views.movies,name="movies"),
    path('read/',views.read_element,name="read"),
    path('del/<id>',views.deletes,name="del"),
    path('upd/<id>',views.up,name="upd"),
    path('form/',views.forms_insert,name="form"),

]