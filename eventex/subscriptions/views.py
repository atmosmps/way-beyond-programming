from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.views.generic import CreateView, DetailView

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription

"""
As requisições chegam nas views, as views são responsáveis por
tratar as informações.

As informações da requisição são direcionadas para o Formulário do Django
que vai tratar o dados e fazer as devidas validações.
"""


class SubscriptionCreate(CreateView):
    model = Subscription
    form_class = SubscriptionForm

    def form_valid(self, form):
        response = super().form_valid(form)
        self.send_email()
        return response

    def send_email(self):
        """Send subscription email"""

        subject = "Confirmação de Inscrição"
        from_ = settings.DEFAULT_FROM_EMAIL
        to = self.object.email
        template_name = "subscriptions/subscription_email.txt"
        context = {"subscription": self.object}

        body = render_to_string(template_name=template_name, context=context)
        mail.send_mail(
            subject=subject, message=body, from_email=from_, recipient_list=[from_, to]
        )


new = SubscriptionCreate.as_view()
detail = DetailView.as_view(model=Subscription)
