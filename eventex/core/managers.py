from django.db.models import Manager, QuerySet

# DEADCODE
# class EmailContactManager(Manager):
#     def get_queryset(self):
#         qs = super().get_queryset()
#         qs = qs.filter(kind=self.model.EMAIL)
#         return qs
#
# DEADCODE
# class PhoneContactManager(Manager):
#     def get_queryset(self):
#         qs = super().get_queryset()
#         qs = qs.filter(kind=self.model.PHONE)
#         return qs


class KindContactQuerySet(QuerySet):
    def emails(self):
        return self.filter(kind=self.model.EMAIL)

    def phones(self):
        return self.filter(kind=self.model.PHONE)


# DEADCODE
# class KindContactManager(Manager):
#     def get_queryset(self):
#         return KindContactQuerySet(self.model, using=self._db)
#
#     def emails(self):
#         return self.get_queryset().emails()
#         # return self.filter(kind=self.model.EMAIL)
#
#     def phones(self):
#         return self.get_queryset().phones()
#         # return self.filter(kind=self.model.PHONE)


class PeriodManager(Manager):
    MIDDAY = "12:00"

    def at_morning(self):
        return self.filter(start__lt=self.MIDDAY)

    def at_afternoon(self):
        return self.filter(start__gte=self.MIDDAY)
