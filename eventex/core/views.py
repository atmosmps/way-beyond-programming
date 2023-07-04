from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from eventex.core.models import Speaker, Talk

home = ListView.as_view(template_name="index.html", model=Speaker)
talk_list = ListView.as_view(model=Talk)


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    # speaker = Speaker.objects.get(slug=slug)
    return render(request, "core/speaker_detail.html", {"speaker": speaker})
