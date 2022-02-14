from django.shortcuts import render, get_object_or_404
from .models import Snippet, Comment, Tag


# Create your views here.
def index(request):
    return render(request, 'club/index.html')


def get_snippets(request):
    snippet_list = Snippet.objects.all()  # big list use objects.find(criteria)
    return render(request, 'club/snippets.html', {'snippet_list': snippet_list})


def get_comments(request):
    comment_list = Comment.objects.all()
    return render(request, 'club/comments.html', {'comment_list': comment_list})


def get_tags(request):
    tag_list = Tag.objects.all()
    return render(request, 'club/tags.html', {'tag_list': tag_list})


def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    return render(request, 'club/snippet_detail.html', {'snippet': snippet})
