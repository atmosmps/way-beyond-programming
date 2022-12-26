from django.shortcuts import resolve_url as r
from django.test import TestCase


class TalkListGet(TestCase):
    def setUp(self) -> None:
        self.response = self.client.get(r("talk_list"))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, "core/talk_list.html")

    def test_html(self):
        ...
