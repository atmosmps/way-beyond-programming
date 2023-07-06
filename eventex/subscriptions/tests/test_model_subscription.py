from datetime import datetime

from django.shortcuts import resolve_url
from django.test import TestCase

from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self) -> None:
        self.obj = Subscription(
            name="Some User Name",
            cpf="12345678901",
            email="some@email.com",
            phone="12-91234-5678",
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_that_the_subscription_must_have_an_auto_created_at_attribute(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str_representation(self):
        self.assertEqual("Some User Name", str(self.obj))

    def test_paid_default_to_false(self):
        """By default, paid must be False"""
        self.assertEqual(False, self.obj.paid)

    def test_get_absolute_url(self):
        url = resolve_url("subscriptions:detail", self.obj.pk)
        self.assertEqual(url, self.obj.get_absolute_url())
