from django.urls import path
from . import views

urlpatterns = [
    path('test', views.welcome),
    path('', views.test),
    path('books', views.get_all_books),
    path('authors', views.get_all_authors),
]
