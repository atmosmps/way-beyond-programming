from django.conf import settings
from django.core import mail
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import DetailView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import FormMixin

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription

"""
As requisições chegam nas views, as views são responsáveis por
tratar as informações.

As informações da requisição são direcionadas para o Formulário do Django
que vai tratar o dados e fazer as devidas validações.
"""


def _send_email(subject, from_, to, template_name, context):
    message = render_to_string(template_name=template_name, context=context)
    mail.send_mail(
        subject=subject, message=message, from_email=from_, recipient_list=[from_, to]
    )


class SubscriptionCreate(TemplateResponseMixin, View):
    template_name = "subscriptions/subscription_form.html"
    form_class = SubscriptionForm

    def get_form(self):
        if self.request.method == "POST":
            return self.form_class(self.request.POST)
        return self.form_class()

    def get_context_data(self, **kwargs):
        context = dict(kwargs)
        context.setdefault("form", self.get_form())
        return context

    def form_invalid(self, form):
        return self.render_to_response(context=self.get_context_data(form=form))

    def form_valid(self, form):
        subscription = form.save()

        _send_email(
            template_name="subscriptions/subscription_email.txt",
            context={"subscription": subscription},
            subject="Confirmação de Inscrição",
            from_=settings.DEFAULT_FROM_EMAIL,
            to=subscription.email,
        )

        return HttpResponseRedirect(subscription.get_absolute_url())

    def get(self, *args, **kwargs):
        return self.render_to_response(context=self.get_context_data())

    def post(self, *args, **kwargs):
        form = self.get_form()

        if not form.is_valid():
            return self.form_invalid(form)
        return self.form_valid(form)


new = SubscriptionCreate.as_view()
detail = DetailView.as_view(model=Subscription)
