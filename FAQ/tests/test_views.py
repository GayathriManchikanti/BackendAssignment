from django.test import TestCase
from django.urls import reverse
from FAQ.models import FAQ
class FAQListViewTest(TestCase):
    def setUp(self):
        # Create a sample FAQ for the test
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a web framework for Python.",
            question_hi="डjango क्या है?",
            question_bn="ডjango কি?",
        )
        self.url = reverse('faq-list')  # Update with your URL name

    def test_faq_list_view(self):
        # Test the FAQ list view with no language specified (defaults to English)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "What is Django?")

    def test_faq_list_view_with_lang(self):
        # Test the FAQ list view with Hindi language
        response = self.client.get(self.url, {'lang': 'hi'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "डjango क्या है?")
