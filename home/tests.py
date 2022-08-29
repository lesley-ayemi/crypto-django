from django.test import TestCase, SimpleTestCase
from django.urls import reverse # used for named urls
# Create your tests here.

class HomePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")
        
    # def test_url_exisits_by_name(self):
    #     response = self.client.get(reverse('home'))
    #     self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'home/index.html')
        
    # def test_template_name_correct(self): # new
    #     response = self.client.get(reverse("home"))
    #     self.assertTemplateUsed(response, "home/index.html")