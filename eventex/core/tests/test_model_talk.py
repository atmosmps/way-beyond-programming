from django.test import TestCase

from eventex.core.models import Talk


class TalkModelTest(TestCase):
    def setUp(self) -> None:
        self.talk = Talk.objects.create(title="Título da Palestra")

    def test_create(self):
        self.assertTrue(Talk.objects.exists())

    def test_has_speakers(self):
        """Talk has many Speakers and vice-versa"""
        self.talk.speakers.create(  # related manager
            name="Atmos Maciel",
            slug="atmos-maciel",
            website="https://atmosmps.me",
        )

        self.assertEqual(1, self.talk.speakers.count())

    def test_description_must_be_blank(self):
        field = Talk._meta.get_field("description")
        self.assertTrue(field.blank)

    def test_speakers_must_be_blank(self):
        field = Talk._meta.get_field("speakers")
        self.assertTrue(field.blank)

    def test_start_must_be_blank(self):
        field = Talk._meta.get_field("start")
        self.assertTrue(field.blank)

    def test_start_must_be_null(self):
        field = Talk._meta.get_field("start")
        self.assertTrue(field.null)

    def test_str(self):
        self.assertEqual('Título da Palestra', str(self.talk))
