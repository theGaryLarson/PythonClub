from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('snippets/', views.get_snippets, name='snippets'),
    path('comments/', views.get_comments, name='comments'),
    path('tags/', views.get_tags, name='tags'),
    path('snippet_detail/<int:snippet_id>', views.snippet_detail, name='snippet_detail'),
    path('newSnippet/', views.newSnippet, name='newSnippet'),
    path('newTag/', views.newTag, name='newTag'),
    path('newComment/', views.newComment, name='newComment'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('loginmessage/', views.login_message, name='loginmessage'),
    path('logoutmessage/', views.logout_message, name='logoutmessage'),

]




