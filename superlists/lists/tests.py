from django.test import Client
from django.test import TestCase

class HomePageTest(TestCase):

    def setUp(self) -> None:
        self.client = Client()

    def test_root_url_resolves_to_home_page_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do Lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

