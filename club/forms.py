from django import forms
from .models import Tag, Snippet, Comment


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = '__all__'


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
