from django.test import TestCase

from eventex.core.models import Talk


class TalkModelTest(TestCase):
    def setUp(self) -> None:
        self.talk = Talk.objects.create(
            title="Título da Palestra",
            start="10:00",
            description="Descrição da palestra",
        )

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
