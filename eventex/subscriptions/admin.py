from django.contrib import admin

from eventex.subscriptions.models import Subscription


class SubscriptionModelAdmin(admin.ModelAdmin):
    # Quais colunas serão exibidas
    list_display = ["name", "email", "phone", "cpf", "created_at"]


admin.site.register(Subscription, SubscriptionModelAdmin)
