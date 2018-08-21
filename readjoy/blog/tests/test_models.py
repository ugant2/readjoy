# from django.test import TestCase, Client
# from blog.models import Post, Profile, Comment, PublishManager
#
#
# class TestMainNavigation(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#
#     def test_homepage(self):
#         home = Client.get('/')
#         self.assertTrue(home.response, 200)
#         self.assertTemplateUsed(home, 'home.html')
#
#     def test_about_us(self):
#         about = Client.get('/about/')
#         self.assertTrue(about.response, 200)
#         self.assertTemplateUsed(about, 'about.html')
#
#     def test_contact_us(self):
#         contact = Client.get('/contact/')
#         self.assertTrue(contact.response, 200)
#         self.assertTemplateUsed(contact, 'contact.html')
#
#     def test_register(self):
#         register = Client.get('/new_register/')
#         self.assertTrue(register.response, 200)
#         self.assertTemplateUsed(register, 'register.html')
#
#     def test_apidoc(self):
#         apidoc = Client.get('/apidoc/')
#         self.assertTrue(apidoc.response, 200)
#         self.assertTemplateUsed(apidoc, 'api_doc.html')

# from django.test.client import Client
#
#
# client = Client()
# response = client.get('/')
# print(response)


