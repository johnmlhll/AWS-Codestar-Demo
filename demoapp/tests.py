from django.test import TestCase, RequestFactory
from demoapp.views.homeViews import HomePageView
from demoapp.views.contactViews import ContactPageView

class HelloWorldTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_home_page(self):
        request = self.factory.get('/')
        response = HomePageView.as_view()(request)
        self.assertEqual(response.get('content-type'), 'text/html; charset=utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Service')

    def test_contact_page(self):
        request = self.factory.get('/contact')
        response = ContactPageView.as_view()(request)
        self.assertEqual(response.get('content-type'), 'text/html; charset=utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Developer')
