from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Article


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.article = Article.objects.create(
            title='this is title',
            body='this is body.this is body.this.',
            author=self.user,
        )

    def test_string_representation(self):
        article = Article(title='sample title')
        self.assertEqual(str(article), article.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.article.get_absolute_url(), '/posts/1/')

    def test_post_content(self):
        self.assertEqual(f'{self.article.author}', 'testuser')
        self.assertEqual(f'{self.article.title}', 'this is title')
        self.assertEqual(f'{self.article.body}',
                         'this is body.this is body.this.')

    def test_home_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogging/index.html')

    def test_article_detail(self):
        response = self.client.get('/posts/1/')
        no_response = self.client.get('/posts/10000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'this is title')
        self.assertTemplateUsed(response, 'blogging/article_detail.html')

    def test_post_create_view(self):
        response = self.client.post(reverse('new_post'), {
            'title': 'new title',
            'body': 'new body',
            'author': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Article.objects.last().title, 'new title')
        self.assertEqual(Article.objects.last().body, 'new body')

    def test_post_update_view(self):
        response = self.client.post(reverse('edit_post', args='1'), {
            'title': 'Updated title',
            'body': 'Updated text',
        })
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.post(
            reverse('delete_post', args='1'))
        self.assertEqual(response.status_code, 302)
