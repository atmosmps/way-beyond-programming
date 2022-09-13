from django.core import mail
from django.shortcuts import resolve_url
from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription

"""
Um tipo de abordagem é cada classe representar um cenário de teste,
ou caso de teste.
"""

SUBSCRIPTION_RESOURCE = "subscriptions:new"


class SubscriptionNewGet(TestCase):
    def setUp(self) -> None:
        self.response = self.client.get(resolve_url(SUBSCRIPTION_RESOURCE))

    def test_get(self):
        """
        GET /inscricao/ must return status code 200
        """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """
        Must use subscriptions/subscription_form.html
        """
        self.assertTemplateUsed(self.response, "subscriptions/subscription_form.html")

    def test_html(self):
        """
        HTML must contain input tags
        """
        tags = (
            ("<form", 1),
            ("<input", 6),
            ('type="text"', 3),
            ('type="email"', 1),
            ('type="submit"', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_should_must_contains_csrf_tokern(self):
        """
        csrfmiddlewaretoken é o nome do campo que o Django criado para este
        template tag csrf.
        """
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_should_has_a_form(self):
        """Context must have subscription form"""
        form = self.response.context["form"]
        self.assertIsInstance(form, SubscriptionForm)


class SubscriptionNewPostValid(TestCase):
    def setUp(self) -> None:
        data = dict(
            name="Some User Name",
            cpf="12345678901",
            email="some@email.com",
            phone="12-91234-5678",
        )

        self.response = self.client.post(resolve_url(SUBSCRIPTION_RESOURCE), data=data)

    def test_post_action(self):
        self.assertEqual(302, self.response.status_code)

    def test_should_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())


class SubscriptionNewPostInvalid(TestCase):
    def setUp(self) -> None:
        self.response = self.client.post(resolve_url(SUBSCRIPTION_RESOURCE), {})

    def test_should_not_redirect_when_request_post_is_invalid(self):
        self.assertEqual(200, self.response.status_code)

    def test_should_that_correct_template_is_used(self):
        self.assertTemplateUsed(self.response, "subscriptions/subscription_form.html")

    def test_should_template_has_a_form(self):
        form = self.response.context["form"]
        self.assertIsInstance(form, SubscriptionForm)

    def test_that_form_has_errors(self):
        form = self.response.context["form"]
        self.assertTrue(form.errors)

    def test_dont_save_subscription(self):
        self.assertFalse(Subscription.objects.exists())


class TemplateRegressionTest(TestCase):
    def test_template_has_non_field_errors(self):
        invalid_data = dict(name="Some User Name", cpf="12345678901")

        response = self.client.post(resolve_url("subscriptions:new"), invalid_data)

        self.assertContains(response, '<ul class="errorlist nonfield">')
