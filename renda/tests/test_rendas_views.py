from django.test import TestCase
from django.urls import resolve, reverse

from renda import views
from renda.models import Renda, TipoRenda
from users.models import User


class RendasViewsTest(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            username='testuser', password='testpassword'
        )

    def test_rendas_create_class_view_is_correct(self):
        view = resolve(reverse('rendas:rendas_create'))
        self.assertIs(view.func.view_class, views.RendasCreateView)

    def test_rendas_list_class_view_is_correct(self):
        view = resolve(reverse('rendas:rendas_list'))
        self.assertIs(view.func.view_class, views.RendasListView)

    def test_rendas_update_class_view_is_correct(self):
        view = resolve(reverse('rendas:rendas_update', kwargs={'id': 1}))
        self.assertIs(view.func.view_class, views.RendasUpdateView)

    def test_rendas_delete_class_view_is_correct(self):
        view = resolve(reverse('rendas:rendas_delete', kwargs={'id': 1}))
        self.assertIs(view.func.view_class, views.RendasDeleteView)

    def test_tipo_rendas_delete_class_view_is_correct(self):
        view = resolve(reverse('rendas:tipo_rendas_delete', kwargs={'id': 1}))
        self.assertIs(view.func.view_class, views.TipoRendasDeleteView)

    def test_rendas_create_view_status_code_200(self):
        user = self.client.force_login(self.user)  # noqa
        response = self.client.get(reverse('rendas:rendas_create'))
        self.assertEqual(response.status_code, 200)

    def test_rendas_list_view_status_code_200(self):
        user = self.client.force_login(self.user)  # noqa
        response = self.client.get(reverse('rendas:rendas_list'))
        self.assertEqual(response.status_code, 200)

    def test_rendas_update_view_status_code_200(self):
        user = self.client.force_login(self.user)  # noqa
        renda = Renda.objects.create(
            owner=self.user, tipo=None, valor=100.00, data='2023-10-01'
        )
        response = self.client.get(
            reverse('rendas:rendas_update', kwargs={'id': renda.pk}))
        self.assertEqual(response.status_code, 200)

    def test_rendas_delete_view_status_code_200(self):
        user = self.client.force_login(self.user)  # noqa
        renda = Renda.objects.create(
            owner=self.user, tipo=None, valor=100.00, data='2023-10-01'
        )
        response = self.client.get(
            reverse('rendas:rendas_delete', kwargs={'id': renda.pk}))
        self.assertEqual(response.status_code, 302)

    def test_tipo_rendas_delete_view_status_code_200(self):
        user = self.client.force_login(self.user)  # noqa
        tipo_renda = TipoRenda.objects.create(
            owner=self.user, nome='Salário'
        )
        response = self.client.get(
            reverse('rendas:tipo_rendas_delete', kwargs={'id': tipo_renda.pk}))
        self.assertEqual(response.status_code, 302)
