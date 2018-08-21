# # from django.test.client import Client
# #
# # client = Client()
# # response = client.get('/')
# # print(response)
#
#
# from django.test import TestCase
# from django.test.client import Client
#
#
# class ViewTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#
#     def test_register_page(self):
#         data = {
#             'username': 'ugant',
#             'email': 'test_ugant@gmai.com',
#             'password': 'pass12345678',
#             'confirm password': 'pass12345678'
#         }
#         response = self.client.post('/new_register/register/', data)
#         self.assertEqual(response.status_code, 302)
#
#
#     def test_login_page(self):
#         data = {
#             'username': 'ugantx',
#             'password': 'wtbkwucbag',
#         }
#         response = self.client.post('/accounts/login/', data)
#         self.assertEqual(response.status_code, 302)
