from django.test import TestCase
from django.contrib.auth.models import User
from menu.models import Page

# Create your tests here.
class MenuListViewTests(TestCase):
    def test_multiple_menu_items(self):
        # Make some test data to be displayed on the page.
        user = User.objects.create()

        Page.objects.create(name="Test item", description="test")
        Page.objects.create(title="Another Test item", description="test")

        # Issue a GET request to the MakeWiki homepage.
        # When we make a request, we get a response back.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the number of pages passed to the template
        # matches the number of pages we have in the database.
        responses = response.context['items']
        self.assertEqual(len(responses), 2)

        self.assertQuerysetEqual(
            responses,
            ['<Page: Test item>', '<Page: Another Test item>'],
            ordered=False
        )
