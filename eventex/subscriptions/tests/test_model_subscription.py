from datetime import datetime

from django.test import TestCase

from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):

    def setUp(self) -> None:
        self.obj = Subscription(
            name="Atmos Maciel",
            cpf="12345678902",
            email="some@email.com",
            phone="98988999999"
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_that_the_subscription_must_have_an_auto_created_at_attribute(
        self
    ):
        self.assertIsInstance(self.obj.created_at, datetime)
