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
