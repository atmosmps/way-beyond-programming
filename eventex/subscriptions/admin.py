from django.contrib import admin
from django.utils.timezone import now
from eventex.subscriptions.models import Subscription


class SubscriptionModelAdmin(admin.ModelAdmin):
    # list_display = quais colunas serão exibidas
    list_display = (
        "name", "email", "phone", "cpf", "created_at", "subscribed_today"
    )
    date_hierarchy = "created_at"

    # search_fields = cria um campo de busca com a prioridade definida na lista
    search_fields = ("name", "email", "phone", "cpf")

    # list_filter = permite filtrar a lista facilmente
    list_filter = ("created_at",)

    def subscribed_today(self, obj):
        return obj.created_at == now().date()

    subscribed_today.short_description = "inscrito hoje?"
    subscribed_today.boolean = True


admin.site.register(Subscription, SubscriptionModelAdmin)
