from django.shortcuts import resolve_url
from django.test import TestCase


class HomeTest(TestCase):
    fixtures = ["Keynotes.json"]

    def setUp(self) -> None:
        self.response = self.client.get(resolve_url("home"))

    def test_should_return_200_status_code_when_root_route_is_accessed(self):
        self.assertEqual(200, self.response.status_code)

    def test_should_return_the_used_template_in_home_page(self):
        self.assertTemplateUsed(self.response, "index.html")

    def test_home_shold_contain_a_subscription_link(self):
        expected = f'href="{resolve_url("subscriptions:new")}"'
        self.assertContains(self.response, expected)

    def test_speakers(self):
        """test must be show speakers in home"""
        speakers = [
            f'href="{resolve_url("speaker_detail", slug="grace-hopper")}"',
            "Grace Hopper",
            "https://hbn.link/hopper-pic",
            f'href="{resolve_url("speaker_detail", slug="alan-turing")}"',
            "Alan Turing",
            "https://hbn.link/turing-pic",
        ]

        for expected in speakers:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_speakers_link(self):
        expected = f'href="{resolve_url("home")}#speakers"'
        self.assertContains(self.response, expected)

    def test_talks_link(self):
        expected = f'href="{resolve_url("talk_list")}'
        self.assertContains(self.response, expected)
