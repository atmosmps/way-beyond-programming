from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription

"""
As requsições chegam nas views, as views são responsáveis por
tratar as informações.

As informações da requisição são direcionadas para o Formulário do Django
que vai tratar o dados e fazer as devidas validações.
"""


def subscribe(request):
    if request.method == "POST":
        return create(request)
    else:
        return new(request)


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        """Abort Return"""
        return render(
            request, "subscriptions/subscription_form.html", context={
                "form": form
            }
        )

    subscription = Subscription.objects.create(**form.cleaned_data)  # the create always return the creted instance # noqa

    _send_email(
        template_name="subscriptions/subscription_email.txt",
        context={'subscription': subscription},
        subject="Confirmação de Inscrição",
        from_=settings.DEFAULT_FROM_EMAIL,
        to=form.cleaned_data["email"],
    )

    return HttpResponseRedirect("/inscricao/{pk}/".format(pk=subscription.pk))


def new(request):
    """
    Envia uma instância de SubscriptionForm para o context do formulário.
    context = contexto usado para renderizar uma resposta, ele é dict like.
    """
    return render(
        request,
        "subscriptions/subscription_form.html",
        context={"form": SubscriptionForm()},
    )


def detail(request):
    from django.http import HttpResponse
    return HttpResponse()


def _send_email(subject, from_, to, template_name, context):
    message = render_to_string(template_name=template_name, context=context)

    mail.send_mail(
        subject=subject, message=message, from_email=from_, recipient_list=[from_, to]
    )
