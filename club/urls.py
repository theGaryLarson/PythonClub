from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('snippets/', views.get_snippets, name='snippets'),
    path('comments/', views.get_comments, name='comments'),
    path('tags/', views.get_tags, name='tags'),
    path('snippet_detail/<int:snippet_id>', views.snippet_detail, name='snippet_detail'),

]


