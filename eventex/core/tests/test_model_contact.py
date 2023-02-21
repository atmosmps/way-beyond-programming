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


class ContactManagerTest(TestCase):
    def setUp(self) -> None:
        s = Speaker.objects.create(
            name="Grace Hopper",
            slug="grace-hopper",
            photo="https://hbn.link/hopper-pic",
        )

        s.contact_set.create(kind=Contact.EMAIL, value="some@email.com")
        s.contact_set.create(kind=Contact.PHONE, value="98988919999")

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ["some@email.com"]
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ["98988919999"]
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)
