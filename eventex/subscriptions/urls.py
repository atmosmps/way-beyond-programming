from django.urls import path

from eventex.subscriptions.views import detail, new

app_name = "subscriptions"

urlpatterns = [
    path("", new, name="new"),
    path("<str:pk>/", detail, name="detail"),
]
