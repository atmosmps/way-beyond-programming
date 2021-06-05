from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

from eventex.subscriptions.forms import SubscriptionForm

"""
As requsições chegam nas views, as views são responsáveis por
tratar as informações.

As informações da requisição são direcionadas para o Formulário do Django
que vai tratar o dados e fazer as devidas validações.
"""


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)

        if form.is_valid():
            body = render_to_string(
                'subscriptions/subscription_email.txt',
                context=form.cleaned_data
            )

            mail.send_mail(
                'Confirmação de Inscrição',
                body,
                settings.FROM_EMAIL,
                [settings.RECIPIENT_LIST, form.cleaned_data['email']]
            )

            """
            messages é o pacote de mensagens do Django.

            Essa mensagem deve ser exibida no Template do Formulário e lá deve
            ser configurada também.

            O Django já adiciona as messages automaticamente no contexto
            do formulário quando existe, através de um context processor.
            """
            messages.success(request, 'Inscrição realizada com sucesso!')
            return HttpResponseRedirect('/inscricao/')
        else:
            return render(
                request, 'subscriptions/subscription_form.html',
                context={'form': form}
            )
    else:
        """
        Envia uma instância de SubscriptionForm para o context do formulário.
        context = contexto usado para renderizar uma resposta, ele é dict like.
        """
        context = {'form': SubscriptionForm()}

        return render(
            request, 'subscriptions/subscription_form.html', context=context
        )
