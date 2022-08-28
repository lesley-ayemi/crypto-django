from django.test import TestCase, SimpleTestCase
# Create your tests here.

class HomePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)