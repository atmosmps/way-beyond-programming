from django.core import mail
from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm

"""
Um tipo de abordagem é cada classe representar um cenário de teste,
ou caso de teste.
"""


class SubscribeFormTest(TestCase):

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
            email="atmos.mps@gmail.com", phone="12-91234-5678"
        )

        self.response = self.client.post('/inscricao/', data=data)

    def test_post_action(self):
        self.assertEqual(302, self.response.status_code)

    def test_should_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_should_have_a_subscription_email_with_subject(self):
        email = mail.outbox[0]
        expected = 'Confirmação de Inscrição'

        self.assertEqual(expected, email.subject)

    def test_should_have_a_subscription_email_with_from(self):
        email = mail.outbox[0]
        expected = 'atmos.mps@gmail.com'

        self.assertEqual(expected, email.from_email)

    def test_should_have_a_subscription_email_with_to(self):
        email = mail.outbox[0]
        expected = ['atmos.mps@gmail.com', 'atmos.mps@gmail.com']

        self.assertEqual(expected, email.to)

    def test_should_have_a_subscription_email_with_body(self):
        email = mail.outbox[0]

        self.assertIn('Atmos Maciel', email.body)
        self.assertIn('12345678901', email.body)
        self.assertIn('atmos.mps@gmail.com', email.body)
        self.assertIn('12-91234-5678', email.body)


class SubscribeInvalidPost(TestCase):

    def setUp(self) -> None:
        self.response = self.client.post('/inscricao/', {})

    def test_should_not_redirect_when_request_post_is_invalid(self):
        self.assertEqual(200, self.response.status_code)

    def test_should_that_correct_template_is_used(self):
        self.assertTemplateUsed(
            self.response, 'subscriptions/subscription_form.html'
        )

    def test_should_template_has_a_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_that_form_has_errors(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)


class SubscribeSuccessMessage(TestCase):
    def setUp(self) -> None:
        data = dict(
            name="Atmos Maciel", cpf="12345678901",
            email="atmos.mps@gmail.com", phone="12-91234-5678"
        )

        # follow=True -> segue com o redirect
        self.response = self.client.post('/inscricao/', data=data, follow=True)

    def test_success_message(self):
        self.assertContains(self.response, 'Inscrição realizada com sucesso!')
