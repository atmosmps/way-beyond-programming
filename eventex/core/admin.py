from django.contrib import admin
from django.utils.html import format_html

from eventex.core.models import Speaker


class SpeakerModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "photo_img", "website_link"]

    def website_link(self, obj):
        # o format_html é igual ao format do python,
        # porém com tratativas para já escapar com segurança marcações HTML
        return format_html('<a href="{0}">{0}</a>', obj.website)

    website_link.shot_description = "website"

    def photo_img(self, obj):
        return format_html('<img width="32px" src="{}"/>', obj.photo)

    photo_img.short_description = "foto"


admin.site.register(Speaker, SpeakerModelAdmin)
