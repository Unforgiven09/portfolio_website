from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='news_index'),
    path("post/<slug:post_slug>/", views.post, name="post"),
    path("author/<str:author>/", views.find_author, name="author"),
    path("tag/<slug:tag_slug>/", views.tag, name="tag"),
    path("all-tags/", views.all_tag, name="all_tags"),
    path("add-news/", views.add_news, name="add_news"),
    path("add-tags/", views.add_tags, name="add_tags"),
    path("change-post/<slug:slug>/", views.change_post, name="change_post"),
    path("search/", views.search, name="search"),
    path('toggle-like/', views.toggle_like, name='toggle_like'),
]