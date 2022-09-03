from uuid import uuid4

from django.conf import settings
from django.core import mail
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.template.loader import render_to_string

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription

"""
As requisições chegam nas views, as views são responsáveis por
tratar as informações.

As informações da requisição são direcionadas para o Formulário do Django
que vai tratar o dados e fazer as devidas validações.
"""


def new(request):
    if request.method == "POST":
        return create(request)

    return empty_form(request)


def empty_form(request):
    """
    Envia uma instância de SubscriptionForm para o context do formulário.
    context = contexto usado para renderizar uma resposta, ele é dict like.
    """
    return render(
        request,
        "subscriptions/subscription_form.html",
        context={"form": SubscriptionForm()},
    )


def create(request):
    form = SubscriptionForm(request.POST)
    form.cleaned_data = {"uuid": uuid4}

    if not form.is_valid():
        """Abort Return"""
        return render(
            request, "subscriptions/subscription_form.html", context={"form": form}
        )

    # the create always return the creted instance # noqa
    subscription = Subscription.objects.create(**form.cleaned_data)

    _send_email(
        template_name="subscriptions/subscription_email.txt",
        context={"subscription": subscription},
        subject="Confirmação de Inscrição",
        from_=settings.DEFAULT_FROM_EMAIL,
        to=subscription.email,
    )

    return HttpResponseRedirect(resolve_url("subscriptions:detail", subscription.uuid))


def detail(request, uuid):
    try:
        subscription = Subscription.objects.get(uuid=uuid)

        return render(
            request=request,
            template_name="subscriptions/subscription_detail.html",
            context={"subscription": subscription},
        )
    except Subscription.DoesNotExist:
        raise Http404


def _send_email(subject, from_, to, template_name, context):
    message = render_to_string(template_name=template_name, context=context)

    mail.send_mail(
        subject=subject, message=message, from_email=from_, recipient_list=[from_, to]
    )
