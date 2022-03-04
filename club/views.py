from django.shortcuts import render, get_object_or_404
from .models import Snippet, Comment, Tag
from .forms import SnippetForm, TagForm, CommentForm
from django.contrib.auth.decorators import login_required


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


@login_required
def newSnippet(request):
    form = SnippetForm
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = SnippetForm()
    else:
        form = SnippetForm()
    return render(request, 'club/newSnippet.html', {'form': form})


@login_required
def newTag(request):
    form = TagForm
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = TagForm()
    else:
        form = TagForm()
    return render(request, 'club/newTag.html', {'form': form})


@login_required
def newComment(request):
    form = CommentForm
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = CommentForm()
    else:
        form = CommentForm()
    return render(request, 'club/newComment.html', {'form': form})


def login_message(request):
    return render(request, 'club/loginmessage.html')


def logout_message(request):
    return render(request, 'club/logoutmessage.html')
