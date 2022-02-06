from django.shortcuts import render
from .models import Snippet
from .models import Comment


# Create your views here.
def index(request):
    return render(request, 'Club/index.html')


def snippets(request):
    snippet_list = Snippet.objects.all()  # big list use objects.find(criteria)
    return render(request, 'Club/snippets.html', {'snippet_list': snippet_list})
