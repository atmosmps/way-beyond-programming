from unittest.mock import Mock

from django.contrib import admin
from django.test import TestCase

from eventex.subscriptions.admin import Subscription, SubscriptionModelAdmin


class SubscriptionModelAdminTest(TestCase):
    def setUp(self) -> None:
        Subscription.objects.create(
            name="Some User Name",
            cpf="12345678901",
            email="some@email.com",
            phone="12-91234-5678",
        )
        self.model_admin = SubscriptionModelAdmin(
            model=Subscription, admin_site=admin.site
        )

        return super().setUp()

    def _call_action(self):
        queryset = Subscription.objects.all()
        original_message = SubscriptionModelAdmin.message_user
        mock = Mock()

        SubscriptionModelAdmin.message_user = mock

        self.model_admin.mark_as_paid(None, queryset)
        SubscriptionModelAdmin.message_user = original_message
        return mock

    def test_has_action(self):
        """Action mark_as_paid must be installed."""
        self._call_action()
        self.assertIn("mark_as_paid", self.model_admin.actions)

    def test_mark_all(self):
        """It's should mark all selected subscriptions as paid."""
        self._call_action()
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())

    def test_message_admin(self):
        """
        It's should send a message to the user

        Testa o comportamento esperado da action.
        Testa o comportamento que deve acontecer quando uma funcionalidade for usada pelo usuário.
        Por isso este é um teste funcional.
        """

        mock = self._call_action()
        mock.assert_called_once_with(
            request=None, message="1 inscriação foi marcada como paga."
        )
