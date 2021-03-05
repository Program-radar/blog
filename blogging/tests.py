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

    def test_post_content(self):
        self.assertEqual(f'{self.article.author}', 'testuser')
        self.assertEqual(f'{self.article.title}', 'this is title')
        self.assertEqual(f'{self.article.body}',
                         'this is body.this is body.this.')

    def test_home_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogging/index.html')
