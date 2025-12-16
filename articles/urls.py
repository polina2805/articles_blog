from django.urls import path
from . import views

app_name = 'articles' 

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('create/', views.ArticleCreateView.as_view(), name='article_create'),
    path('<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
]