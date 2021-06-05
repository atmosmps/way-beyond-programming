from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

from eventex.subscriptions.forms import SubscriptionForm

"""
As requsições chegam nas views, as views são responsáveis por
tratar as informações.

As informações da requisição são direcionadas para o Formulário do Django
que vai tratar o dados e fazer as devidas validações. Uma vez validados,
os dados

"""


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        form.full_clean()

        body = render_to_string(
            'subscriptions/subscription_email.txt', context=form.cleaned_data
        )

        mail.send_mail(
            'Confirmação de Inscrição',
            body,
            'contato@eventex.com',
            ['contato@eventex.com', form.cleaned_data['email']]
        )

        return HttpResponseRedirect('/inscricao/')
    else:
        """
        Envia uma instância de SubscriptionForm para o context do formulário.
        context = contexto usado para renderizar uma resposta, ele é dict like.
        """
        context = {'form': SubscriptionForm()}

        return render(
            request, 'subscriptions/subscription_form.html', context=context
        )
