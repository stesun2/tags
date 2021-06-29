from django.test import SimpleTestCase

# Create your tests here.
class TagsTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
