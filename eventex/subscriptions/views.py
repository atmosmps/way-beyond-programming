from django.shortcuts import render

from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    """
    Envia uma instância de SubscriptionForm para o context do formulário.
    context = contexto usado para renderizar uma resposta, ele é dict like.
    """
    context = {'form': SubscriptionForm()}

    return render(
        request, 'subscriptions/subscription_form.html', context=context
    )
