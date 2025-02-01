from django.test import TestCase
from FAQ.models import FAQ

class FAQModelTests(TestCase):
    def test_create_faq(self):
        faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a high-level Python web framework.",
        )
        self.assertEqual(faq.question, "What is Django?")
        self.assertEqual(faq.answer, "Django is a high-level Python web framework.")
