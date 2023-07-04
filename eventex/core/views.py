from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from eventex.core.models import Speaker, Talk


home = ListView.as_view(
    template_name="index.html",
    model=Speaker
)


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    # speaker = Speaker.objects.get(slug=slug)
    return render(request, "core/speaker_detail.html", {"speaker": speaker})


def talk_list(request):
    # DEADCODE
    # context = {
    #     "morning_talks": Talk.objects.at_morning(),
    #     # "morning_talks": Talk.objects.filter(start__lt="12:00"), # less than # noqa
    #     "afternoon_talks": Talk.objects.at_afternoon(),
    #     # "afternoon_talks": Talk.objects.filter(start__gte="12:00"), # grater than or equal # noqa,
    #     "courses": Course.objects.all(),
    # }
    context = {
        "morning_talks": Talk.objects.at_morning(),
        "afternoon_talks": Talk.objects.at_afternoon(),
    }
    return render(request, "core/talk_list.html", context)
