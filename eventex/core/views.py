from django.shortcuts import get_object_or_404, render

from eventex.core.models import Speaker, Talk


def home(request):
    speakers = Speaker.objects.all()
    return render(request, "index.html", context={"speakers": speakers})


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    # speaker = Speaker.objects.get(slug=slug)
    return render(request, "core/speaker_detail.html", {"speaker": speaker})


def talk_list(request):
    speaker = Speaker(name="Some Name", slug="some-name")
    courses = [
        dict(
            title="Título do curso",
            start="09:00",
            description="Descrição do curso.",
            speakers={"all": [speaker]},
        )
    ]
    context = {
        "morning_talks": Talk.objects.at_morning(),
        # "morning_talks": Talk.objects.filter(start__lt="12:00"), # less than
        "afternoon_talks": Talk.objects.at_afternoon(),
        # "afternoon_talks": Talk.objects.filter(start__gte="12:00"), # grater than or equal # noqa,
        "courses": courses,
    }
    return render(request, "core/talk_list.html", context)
