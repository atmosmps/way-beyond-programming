from django.conf import settings
from django.core import mail
from django.shortcuts import resolve_url
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self) -> None:
        data = dict(
            name="Some User Name",
            cpf="12345678901",
            email=settings.DEFAULT_FROM_EMAIL,
            phone="12-91234-5678",
        )

        self.client.post(resolve_url("subscriptions:new"), data=data)
        self.email = mail.outbox[0]

    def test_should_have_a_subscription_email_with_subject(self):
        expected = "Confirmação de Inscrição"
        self.assertEqual(expected, self.email.subject)

    def test_should_have_a_subscription_email_with_from(self):
        expected = settings.DEFAULT_FROM_EMAIL
        self.assertEqual(expected, self.email.from_email)

    def test_should_have_a_subscription_email_with_to(self):
        expected = [settings.DEFAULT_FROM_EMAIL, settings.DEFAULT_FROM_EMAIL]
        self.assertEqual(expected, self.email.to)

    def test_should_have_a_subscription_email_with_body(self):
        contents = [
            "Some User Name",
            "12345678901",
            settings.DEFAULT_FROM_EMAIL,
            "12-91234-5678",
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
