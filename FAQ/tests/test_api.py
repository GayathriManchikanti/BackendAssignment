from rest_framework.test import APITestCase
from rest_framework import status
from FAQ.models import FAQ

class FAQApiTest(APITestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a web framework for Python.",
            question_hi="डjango क्या है?",
            question_bn="ডjango কি?",
        )
        self.url = '/api/faqs/'

    def test_get_faqs(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "What is Django?")

    def test_get_faqs_with_lang(self):
        response = self.client.get(self.url, {'lang': 'hi'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "डjango क्या है?")

    def test_get_faqs_with_invalid_lang(self):
        response = self.client.get(self.url, {'lang': 'invalid'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "What is Django?")
