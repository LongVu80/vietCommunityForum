
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="index"), 
    path('create', views.post_create, name='create'),
    path('feed/', views.feed, name='feed'),
     path('feed2/', views.feed, name='feed2'),
    path('listItems', views.listItems, name='listItems'),
    path('like/<int:id>', views.like_post, name='like'),
    path('posts/<int:id>/', views.detail, name='detail'),
    path('posts/<slug:slug>/', views.detail, name='detail'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('view', views.post_view, name='view'),
    path('add_feed_reply/<int:comment_id>/', views.add_feed_reply, name='add_feed_reply'),
    path('add_reply/<int:comment_id>/', views.add_reply, name='add_reply'),
]