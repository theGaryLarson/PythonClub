import datetime
from .views import index, get_tags, get_comments, get_snippets, snippet_detail
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.test import TestCase

from PythonClub import settings
from .models import Tag, Snippet, Comment


# Create your tests here.


class TagTestCase(TestCase):
    def setup(self):
        test_tag = Tag()
        test_tag.keyword = "Beginner"
        test_tag.tag_description = "Code focused on syntax and entry level programming techniques."
        return test_tag

    def test_table(self):
        self.assertEqual(str(Tag._meta.db_table), 'tag')

    def test_table_plural(self):
        self.assertEqual(str(Tag._meta.verbose_name_plural), 'tags')

    def test_string(self):
        tag = self.setup()
        self.assertEqual(str(tag), tag.keyword)

    def test_keyword(self):
        tag = self.setup()
        self.assertEqual(tag.keyword, "Beginner")

    def test_description(self):
        tag = self.setup()
        self.assertEqual(tag.tag_description, "Code focused on syntax and entry level programming techniques.")


class SnippetTestCase(TestCase):
    def setup(self):
        test = Snippet()
        test.snippet_title = "Making Web Request"
        # todo: look at documentation
        # test.tag = "Web Scraping"
        test.user = User()
        test.user.username = 'garyl'
        test.snippet_entrydate = datetime.date.today()
        test.reference_url = "https://www.google.com"
        test.code_snippet = "print(hello world!)"
        return test

    def test_table(self):
        self.assertEqual(str(Snippet._meta.db_table), 'snippet')

    def test_table_plural(self):
        self.assertEqual(str(Snippet._meta.verbose_name_plural), 'snippets')

    def test_title(self):
        snippet = self.setup()
        self.assertEqual(snippet.snippet_title, 'Making Web Request')

    # todo: get tags assigned and tested
    # def test_tag(self):
    #     snippet = self.setup()
    #     self.assertEqual(snippet.tag, 'Beginner')

    def test_user(self):
        snippet = self.setup()
        self.assertEqual(snippet.user.username, 'garyl')

    def test_entrydate(self):
        snippet = self.setup()
        self.assertEqual(snippet.snippet_entrydate, datetime.date.today())

    def test_url(self):
        snippet = self.setup()
        self.assertEqual(snippet.reference_url, 'https://www.google.com')

    def test_code_snippet(self):
        snippet = self.setup()
        self.assertEqual(snippet.code_snippet, 'print(hello world!)')


class CommentTestCase(TestCase):
    def setup(self):
        test = Comment()
        test.comment_title = "Making Web Request"
        test.comment_date = datetime.date.today()
        test.snippet = Snippet()
        test.snippet.snippet_title = 'snippet title'
        # todo: look up documentation to test many to many relationships
        # user = User.objects.create(username='garyl')
        # test.user.set([user.pk])
        test.snippet_rating = 5
        test.discussion_text = 'Let us talk about this ...'
        return test

    def test_table(self):
        self.assertEqual(str(Comment._meta.db_table), 'comment')

    def test_table_plural(self):
        self.assertEqual(str(Comment._meta.verbose_name_plural), 'comments')

    def test_title(self):
        comment = self.setup()
        self.assertEqual(comment.comment_title, 'Making Web Request')

    def test_date(self):
        comment = self.setup()
        self.assertEqual(comment.comment_date, datetime.date.today())

    def test_snippet(self):
        comment = self.setup()
        self.assertEqual(comment.snippet.snippet_title, 'snippet title')

    # todo: get this working
    # def test_user(self):
    #     comment = self.setup()
    #     self.assertEqual(comment.user.username, 'garyl')

    def test_rating(self):
        comment = self.setup()
        self.assertEqual(comment.snippet_rating, 5)

    def test_discussion_test(self):
        comment = self.setup()
        self.assertEqual(comment.discussion_text, 'Let us talk about this ...')


class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class GetSnippetsTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('snippets'))
        self.assertEqual(response.status_code, 200)


class GetCommentsTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('comments'))
        self.assertEqual(response.status_code, 200)


class GetTagsTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('tags'))
        self.assertEqual(response.status_code, 200)


class GetSnippetDetail(TestCase):
    # todo: many to many setup for details isn't working getting same error as above
    # todo: Snippet.tag(many to many) Comment.user(many to many)
    def setup(self):
        self.user = User.objects.create(username='myuser')
        self.tag = Tag.objects.create(keyword='Beginner')
        self.snip = Snippet.objects.create(snippet_title='snippetTitle',
                                           tag=self.tag,
                                           user=self.user,
                                           snippet_entrydate=datetime.date.today(),
                                           reference_url='https://www.google.com',
                                           code_snippet='codeSnippet')

        self.comment1 = Comment.objects.create(comment_title='snippetreview',
                                               comment_date=datetime.date.today(),
                                               snippet=self.snip,
                                               discussion_test='discussion about snippet')

        self.comment2 = Comment.objects.create(comment_title='snippetreview',
                                               comment_date=datetime.date.today(),
                                               snippet=self.snip,
                                               discussion_test='discussion about snippet')
        self.comment1.user.add(self.user)
        self.comment2.user.add(self.user)

    # todo: research why many to many is not working
    # def test_number_of_reviews(self):
    #     self.setup()
    #     comments = Comment.objects.filter(product=self.snip).count()
    #     self.assertEqual(comments, 2)

    # def test_snippet_detail_success(self):
    #     self.setup()
    #     response = self.client.get(reverse('snippet_detail', args=(self.snip.id,)))
    #     # Assert that self.post is actually returned by the post_detail view
    #     self.assertEqual(response.status_code, 200)


# todo: more research.. Why is this expecting a 200 message and receiving a 404
class NewSnippetAuthenticationTest(TestCase):
    def setup(self):
        self.test_user = User.objects.create_user(username='testuser1', password='p@ssw0rd1')
        self.tag = Tag.create.objects.create(keyword='beginner', tag_description='Covers Syntax')
        self.snippet = Snippet.objects.create(snippet_title='Our First Program',
                                              snippet_entrydate=datetime.date.today(),
                                              reference_url='https://www.google.com',
                                              code_snippet='print(\'Hello World!\'', user=self.test_user,
                                              tag=self.tag)

    def testRedirectIfNotLoggedIn(self):
        response = self.client.get(reverse('newSnippet'))
        self.assertRedirects(response, '/accounts/login/?next=/club/newSnippet')
