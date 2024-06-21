from django.test import TestCase, Client
from django.urls import reverse
from main.models import Article
from datetime import datetime


class ArticleViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()

        # Create test data
        self.article1 = Article.objects.create(
            title='Test Article 1',
            content='Content for test article 1',
            publication_date=datetime.now()
        )

    def test_article_detail_view(self):
        url = reverse('main:article_detail', args=[self.article1.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article_detail.html')
        self.assertContains(response, self.article1.title)
        self.assertContains(response, self.article1.content)
