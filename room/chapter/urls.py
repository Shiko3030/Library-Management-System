from django.urls import path
from . import views

urlpatterns = [
path('',views.index, name="index"),
path('books/',views.books, name="books"),
path('delete/<str:i_d>/',views.delete, name="delete"),
path('update/<str:i_d>/',views.update, name="update"),


]
