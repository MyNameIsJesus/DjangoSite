from django.urls import path
from . import views
urlpatterns = [
    path('', views.MyNews, name='newspage'),
    path('create', views.CreateNews, name='create'),
    path('<int:pk>', views.news_detail_views.as_view(), name='news-detail'),
    path('<int:pk>/update', views.news_update_views.as_view(), name='news-update'),
    path('<int:pk>/delete', views.news_delete_views.as_view(), name='news-delete'),
]