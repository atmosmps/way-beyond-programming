from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):

    def setUp(self) -> None:
        data = dict(
            name="Atmos Maciel", cpf="12345678901",
            email="atmos.mps@gmail.com", phone="12-91234-5678"
        )

        self.client.post('/inscricao/', data=data)
        self.email = mail.outbox[0]

    def test_should_have_a_subscription_email_with_subject(self):
        expected = 'Confirmação de Inscrição'
        self.assertEqual(expected, self.email.subject)

    def test_should_have_a_subscription_email_with_from(self):
        expected = 'contato@eventex.com.br'
        self.assertEqual(expected, self.email.from_email)

    def test_should_have_a_subscription_email_with_to(self):
        expected = ['contato@eventex.com.br', 'atmos.mps@gmail.com']
        self.assertEqual(expected, self.email.to)

    def test_should_have_a_subscription_email_with_body(self):
        contents = [
            'Atmos Maciel',
            '12345678901',
            'atmos.mps@gmail.com',
            '12-91234-5678',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
