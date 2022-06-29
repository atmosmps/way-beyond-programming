from django.test import TestCase


class HomeTest(TestCase):
    def setUp(self) -> None:
        self.response = self.client.get("/")

    def test_should_return_200_status_code_when_root_route_is_accessed(self):
        self.assertEqual(200, self.response.status_code)

    def test_should_return_the_used_template_in_home_page(self):
        self.assertTemplateUsed(self.response, "index.html")

    def test_home_shold_contain_a_subscription_link(self):
        self.assertContains(self.response, 'href="/inscricao/"')
