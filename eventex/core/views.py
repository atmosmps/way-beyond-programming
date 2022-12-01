from django.shortcuts import render


def home(request):
    speakers = [
        {
            "name": "Grace Hopper",
            "photo": "https://hbn.link/hopper-pic",
        },
        {
            "name": "Alan Turing",
            "photo": "https://hbn.link/turing-pic",
        },
    ]
    return render(request, "index.html", context={"speakers": speakers})
