from django.db import models
from django.shortcuts import resolve_url


class Speaker(models.Model):
    name = models.CharField(verbose_name="nome", max_length=255)
    slug = models.SlugField(verbose_name="slug")
    photo = models.URLField(verbose_name="foto")
    website = models.URLField(verbose_name="website", blank=True)
    description = models.TextField(verbose_name="descrição", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Palestrante"
        verbose_name_plural = "Palestrantes"

    def get_absolute_url(self):
        return resolve_url("speaker_detail", self.slug)


class Contact(models.Model):
    EMAIL = "E"
    PHONE = "P"
    KINDS = (
        (EMAIL, "Email"),
        (PHONE, "Telefone"),
    )
    # é melhor usar a definição de um relacionamento definindo o modelo
    # string, dessa maneira o Django internamente consegue definir qual a
    # relação interna entre os models, sem a necessidade de ficar realizando
    # imports entre os módulos, isso é importante principalmente entre modelos
    # que estão em módulos/apps diferentes pois evita imports circulares.
    speaker = models.ForeignKey(
        "Speaker", on_delete=models.CASCADE, verbose_name="palestrante"
    )
    kind = models.CharField(verbose_name="tipo", max_length=1, choices=KINDS)
    value = models.CharField(verbose_name="valor", max_length=255)

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

    def __str__(self):
        return self.value
