from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles_list, name='articles_list'),
    path('create/', views.create_article, name='create_article'),
    path('<int:id>/edit/', views.edit_article, name='edit_article'),
]