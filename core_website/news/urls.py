from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='news_index'),
    path("post/<slug:title>/", views.post, name="post"),
    path("tag/<str:name>/", views.tag, name="tag"),
    path("all-tags/", views.all_tag, name="all_tags"),
    path("add-news/", views.add_news, name="add_news"),
    path("add-tags/", views.add_tags, name="add_tags"),
    path("change-post/<slug:slug>/", views.change_post, name="change_post"),
]