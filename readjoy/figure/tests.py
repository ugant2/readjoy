
from django.test import TestCase, Client
from blog.models import Post, Profile, Comment


class TestMainNavigation(TestCase):

    def setUp(self):
        self.client = Client()

    def test_homepage(self):
        response = self.client.get('/')
        self.assertTrue(response.status_code, 200)

    def test_about_us(self):
        response = self.client.get('/about/about_pg/')
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        response = self.client.get('/new_register/register/')
        self.assertEqual(response.status_code, 200)

    def test_register_page_post(self):
        data = {
            'Username': 'test_ram',
            'Password': 'password_test2',
            'Password confirmation': 'password_test2',
        }
        response = self.client.post('/new_register/register/', data)
        self.assertEqual(response.status_code, 200)

    def test_contact_us_page(self):
        response = self.client.get('/contact/contact_pg/')
        self.assertTrue(response.status_code, 200)

    def test_apidoc_page(self):
        response = self.client.get('/apidoc/api_doc/')
        self.assertTrue(response.status_code, 200)

    def test_userManual_page(self):
        response = self.client.get('/manual/manual/')
        self.assertEqual(response.status_code, 200)

    def test_detail_page(self):
        response = self.client.get('/detail/(?P<pk>\d+)/detail_pg/')
        self.assertEqual(response.status_code, 200)




#
# from django.test import TestCase
# from blog.views import HomeListView
#
# try:
#     from django.core.urlresolvers import reverse
# except ImportError:
#     from django.urls import reverse
#
#
# # Create your tests here.
#
# class HomeTests(TestCase):
#     def test_home_view_status_code(self):
#         url = reverse('HomeListView')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
