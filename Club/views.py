from django.shortcuts import render
from .models import Snippet, Comment, Tag


# Create your views here.
def index(request):
    return render(request, 'Club/index.html')


def snippets(request):
    snippet_list = Snippet.objects.all()  # big list use objects.find(criteria)
    return render(request, 'Club/snippets.html', {'snippet_list': snippet_list})


def comments(request):
    comment_list = Comment.objects.all()
    return render(request, 'Club/comments.html', {'comment_list': comment_list})


def tags(request):
    tag_list = Tag.objects.all()
    return render(request, 'Club/tags.html', {'tag_list': tag_list})
