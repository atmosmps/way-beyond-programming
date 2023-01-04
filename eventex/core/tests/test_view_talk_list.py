from django.shortcuts import resolve_url as r
from django.test import TestCase

from eventex.core.models import Speaker, Talk


class TalkListGet(TestCase):
    def setUp(self) -> None:
        t1 = Talk.objects.create(
            title="Título da Palestra",
            start="10:00",
            description="Descrição da palestra",
        )
        t2 = Talk.objects.create(
            title="Título da Palestra",
            start="13:00",
            description="Descrição da palestra",
        )

        speaker = Speaker.objects.create(
            name="Atmos Maciel",
            slug="atmos-maciel",
            website="https://atmosmps.me",
        )

        t1.speakers.add(speaker)
        t2.speakers.add(speaker)

        self.response = self.client.get(r("talk_list"))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, "core/talk_list.html")

    def test_html(self):
        contents = [
            (2, "Título da Palestra"),
            (1, "10:00"),
            (1, "13:00"),
            (2, "/palestrantes/atmos-maciel"),
            (2, "Atmos Maciel"),
            (2, "Descrição da palestra"),
        ]
        for count, expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected, count)

    def test_context(self):
        context_variables = ["morning_talks", "afternoon_talks"]

        for key in context_variables:
            with self.subTest():
                self.assertIn(key, self.response.context)
