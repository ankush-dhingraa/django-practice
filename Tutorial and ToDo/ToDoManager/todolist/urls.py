from django.urls import path , include
from todolist import views
urlpatterns = [
    path('/', views.home, name="Home Page"),
    path('contact-us/', views.contact, name="Contact us Page"),
    path('about-us/', views.about, name="About us page"),
    path('todolist/', views.todolist, name="Todo list"),

]
