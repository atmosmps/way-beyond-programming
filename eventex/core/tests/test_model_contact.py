from django.core.exceptions import ValidationError
from django.test import TestCase

from eventex.core.models import Contact, Speaker


class ContactModelTest(TestCase):
    def setUp(self) -> None:
        self.speaker = Speaker.objects.create(
            name="Some Name", slug="some-name", photo="https://somelink/pic"
        )

    def test_email(self):
        Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value="some@email.com",
        )

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.PHONE,
            value="98988989898",
        )

        self.assertTrue(Contact.objects.exists())

    def test_model_choices(self):
        """Contact kind should be limited to E or P"""
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind="A",
            value="B",
        )

        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value="some@email.com",
        )
        self.assertEqual("some@email.com", str(contact))
