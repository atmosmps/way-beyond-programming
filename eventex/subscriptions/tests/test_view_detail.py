from django.shortcuts import resolve_url
from django.test import TestCase

from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    def setUp(self) -> None:
        self.obj = Subscription.objects.create(
            name="Some User Name",
            cpf="12345678901",
            email="some@email.com",
            phone="12-91234-5678",
        )
        self.resp = self.client.get(resolve_url("subscriptions:detail", self.obj.uuid))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, "subscriptions/subscription_detail.html")

    def test_context(self):
        subscription = self.resp.context["subscription"]
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = (self.obj.name, self.obj.cpf, self.obj.email, self.obj.phone)
        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)


class SubscriptionDetailNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get(
            resolve_url(
                "subscriptions:detail",
                "695837ef-4218-4106-82b1-af4b1acc9970",
            )
        )
        self.assertEqual(404, resp.status_code)
