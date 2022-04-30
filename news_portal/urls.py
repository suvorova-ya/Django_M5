from django.urls import path
from. import views
from .views import UserUpdateView


urlpatterns = [
    path('',views.news.as_view(),name = "news"),
    path('create',views.PostCreateView.as_view(), name='news_create'),  # Ссылка на создание новости
    path('<int:pk>',views.NewsDetail.as_view(),name = 'details_view'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='news_create'),  # Ссылка на обновление новости
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='news_delete'),  # Ссылка на удаление новости
    path('user_update', UserUpdateView.as_view(), name='user_update'),  # Ссылка на обновление профиля
    path('post-like/<int:pk>', views.PostLike, name="post_like"),
]