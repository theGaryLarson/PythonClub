from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
# keyword associated with python code snippet
class Tag(models.Model):
    # remember primary key is essentially set to autoincrement
    keyword = models.CharField(max_length=255)
    tag_description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.keyword

    class Meta:
        db_table = 'tag'
        verbose_name_plural = 'tags'


class Snippet(models.Model):
    snippet_title = models.CharField(max_length=255)
    tag = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    snippet_entrydate = models.DateField()  # datetime.datetime.now()
    reference_url = models.URLField(null=True, blank=True)
    code_snippet = models.TextField()

    def __str__(self):
        return self.snippet_title

    class Meta:
        db_table = 'snippet'
        verbose_name_plural = 'snippets'


class Comment(models.Model):
    comment_title = models.CharField(max_length=255)
    comment_date = models.DateField()  # datetime.datetime.now()
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)
    snippet_rating = models.SmallIntegerField()
    discussion_text = models.TextField()

    def __str__(self):
        return self.comment_title

    class Meta:
        db_table = 'comment'  # if not set will include project name with table. Giving us a long String
        verbose_name_plural = 'comments'
