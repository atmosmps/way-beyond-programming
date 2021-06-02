from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):

    def setUp(self) -> None:
        self.response = self.client.get('/inscricao/')

    def test_get(self):
        """
        GET /inscricao/ must return status code 200
        """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """
        Must use subscriptions/subscription_form.html
        """
        self.assertTemplateUsed(
            self.response, 'subscriptions/subscription_form.html'
        )

    def test_html(self):
        """
        HTML must contain input tags
        """

        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 6)
        self.assertContains(self.response, 'type="text"', 3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def test_should_must_contains_csrf_tokern(self):
        """
        csrfmiddlewaretoken é o nome do campo que o Django criado para este
        template tag csrf.
        """
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_should_has_a_form(self):
        """Context must have subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_should_form_has_four_fields(self):
        form = self.response.context['form']
        self.assertSequenceEqual(
            ['name', 'cpf', 'email', 'phone'], list(form.fields)
        )


class SubscriptionTest(TestCase):

    def setUp(self) -> None:
        data = dict(
            name="Atmos Maciel", cpf="12345678901",
            email="atmos@email.com", phone="12-91234-5678"
        )

        self.response = self.client.post('/inscricao/', data=data)

    def test_post_action(self):
        self.assertEqual(302, self.response.status_code)

    def test_should_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_should_sent_email_with_subscription_email_subject(self):
        email = mail.outbox[0]
        expected = 'Confirmação de Inscrição'

        self.assertEqual(expected, email.subject)

    def test_should_sent_email_with_subscription_email_from(self):
        email = mail.outbox[0]
        expected = 'contato@eventex.com'

        self.assertEqual(expected, email.from_email)
