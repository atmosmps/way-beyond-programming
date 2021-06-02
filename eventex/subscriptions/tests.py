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


