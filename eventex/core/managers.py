from django.db.models import Manager, QuerySet


class KindContactQuerySet(QuerySet):
    def emails(self):
        return self.filter(kind=self.model.EMAIL)

    def phones(self):
        return self.filter(kind=self.model.PHONE)


class PeriodQuerySet(QuerySet):
    MIDDAY = "12:00"

    def at_morning(self):
        return self.filter(start__lt=self.MIDDAY)

    def at_afternoon(self):
        return self.filter(start__gte=self.MIDDAY)


PeriodManager = Manager.from_queryset(PeriodQuerySet)
