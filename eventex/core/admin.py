from django.contrib import admin
from django.utils.html import format_html

from eventex.core.models import Contact, Course, Speaker, Talk


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1  # configura quantos campos vazios devem ser apresentados no admin # noqa


class SpeakerModelAdmin(admin.ModelAdmin):
    inlines = [ContactInline]
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "photo_img", "website_link"]

    def website_link(self, obj):
        # o format_html é igual ao format do python,
        # porém com tratativas para já escapar com segurança marcações HTML
        return format_html('<a href="{0}">{0}</a>', obj.website)

    website_link.shot_description = "website"

    def photo_img(self, obj):
        return format_html('<img width="32px" src="{}"/>', obj.photo)

    photo_img.allow_tags = True
    photo_img.short_description = "foto"

    def email(self, obj):
        return obj.contact_set.emails().first()
        # return obj.contact_set(manager='emails').first()

    def phone(self, obj):
        return obj.contact_set.phones().first()
        # return obj.contact_set(manager='phones').first()


class TalkModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(course=None)


admin.site.register(Speaker, SpeakerModelAdmin)
admin.site.register(Talk, TalkModelAdmin)
admin.site.register(Course)
