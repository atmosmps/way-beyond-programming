import uuid

from django.db import models


class Subscription(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(verbose_name="nome", max_length=100)
    cpf = models.CharField(verbose_name="cpf", max_length=11)
    email = models.EmailField(verbose_name="email")
    phone = models.CharField(verbose_name="telefone", max_length=20)
    created_at = models.DateTimeField(verbose_name="criado em", auto_now_add=True)

    class Meta:
        verbose_name = "inscrição"
        verbose_name_plural = "inscrições"
        ordering = (
            "-created_at",
        )  # indica que o model será ordenado de maneira decrescente  # noqa

    def __str__(self):
        return self.name
