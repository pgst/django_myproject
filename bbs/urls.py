from django.urls import path
from . import views


app_name = 'bbs'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateView.as_view(), name='create'),
    # path('<int:pk>/update/', views.article_update, name='article_update'),
    # path('<int:pk>/delete/', views.article_delete, name='article_delete'),
    # path('comment/create/', views.comment_create, name='comment_create'),
    # path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
]