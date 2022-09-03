from django.conf import settings
from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def make_validated_form(self, **kwargs):
        valid_data = dict(
            name="Some User Name",
            cpf="12345678901",
            email=settings.DEFAULT_FROM_EMAIL,
            phone="12-91234-5678",
        )

        data = dict(valid_data, **kwargs)

        form = SubscriptionForm(data=data)
        form.is_valid()

        return form

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def test_should_form_has_four_fields(self):
        form = SubscriptionForm()
        expected = ["name", "cpf", "email", "phone"]
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """CPF must only accept digits"""
        form = self.make_validated_form(cpf="ABCD1234567")
        # self.assertFormErrorMessage(form, "cpf", "CPF deve conter apenas números")
        self.assertFormErrorCode(form, "cpf", "digits")

    def test_cpf_has_eleven_digits(self):
        """CPF must have 11 digits"""
        form = self.make_validated_form(cpf="1234")
        # self.assertFormErrorMessage(form, "cpf", "CPF deve conter 11 números")
        self.assertFormErrorCode(form, "cpf", "length")
