from django.contrib import admin
from django.utils.timezone import now

from eventex.subscriptions.models import Subscription


class SubscriptionModelAdmin(admin.ModelAdmin):
    # list_display = quais colunas serão exibidas
    list_display = (
        "name",
        "email",
        "phone",
        "cpf",
        "created_at",
        "subscribed_today",
        "paid",
    )
    date_hierarchy = "created_at"

    # search_fields = cria um campo de busca com a prioridade definida na lista
    search_fields = ("name", "email", "phone", "cpf")

    # list_filter = permite filtrar a lista facilmente
    list_filter = ("created_at", "paid")

    actions = ["mark_as_paid"]

    def subscribed_today(self, obj):
        return obj.created_at == now().date()

    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)
        if count == 1:
            msg = "{count} inscriação foi marcada como paga."
        else:
            msg = "{count} inscrições foram marcadas como pagas."

        self.message_user(request=request, message=msg.format(count=count))

    mark_as_paid.short_description = "Marcar como pago"
    subscribed_today.short_description = "inscrito hoje?"
    subscribed_today.boolean = True


admin.site.register(Subscription, SubscriptionModelAdmin)
