from django.test import TestCase

from eventex.core.models import Contact, Speaker


class ContactModelTest(TestCase):
    def test_create(self):
        speaker = Speaker.objects.create(
            name="Some Name", slug="some-name", photo="https://somelink/pic"
        )

        contact = Contact.objects.create(
            speaker=speaker,
            kind="E",
            value="some@email.com",
        )

        self.assertTrue(Contact.objects.exists())
