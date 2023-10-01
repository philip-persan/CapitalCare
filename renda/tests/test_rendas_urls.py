from django.test import TestCase
from django.urls import reverse


class RendasURLsTest(TestCase):

    def test_rendas_create_url_is_correct(self):
        rendas_list_url = reverse('rendas:rendas_create')
        self.assertEqual(rendas_list_url, '/rendas/create/')

    def test_rendas_list_url_is_correct(self):
        rendas_list_url = reverse('rendas:rendas_list')
        self.assertEqual(rendas_list_url, '/rendas/list/')

    def test_rendas_update_url_is_correct(self):
        rendas_list_url = reverse('rendas:rendas_update', kwargs={'id': 1})
        self.assertEqual(rendas_list_url, '/rendas/update/1/')

    def test_rendas_delete_url_is_correct(self):
        rendas_list_url = reverse('rendas:rendas_delete', kwargs={'id': 1})
        self.assertEqual(rendas_list_url, '/rendas/delete/1/')

    def test_tipo_rendas_delete_url_is_correct(self):
        rendas_list_url = reverse(
            'rendas:tipo_rendas_delete', kwargs={'id': 1})
        self.assertEqual(rendas_list_url, '/rendas/delete/tipo/1/')
