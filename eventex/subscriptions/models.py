import uuid

from django.db import models

from eventex.subscriptions.validators import validate_cpf


class Subscription(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(verbose_name="nome", max_length=100)
    cpf = models.CharField(verbose_name="cpf", max_length=11, validators=[validate_cpf])
    email = models.EmailField(verbose_name="email", blank=True)
    phone = models.CharField(verbose_name="telefone", max_length=20, blank=True)
    created_at = models.DateTimeField(verbose_name="criado em", auto_now_add=True)
    paid = models.BooleanField(verbose_name="pago", default=False)

    class Meta:
        verbose_name = "inscrição"
        verbose_name_plural = "inscrições"
        ordering = (  # indica que o model será ordenado de maneira decrescente
            "-created_at",
        )

    def __str__(self):
        return self.name
