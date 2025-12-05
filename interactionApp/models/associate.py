from django.db import models
from django.utils import timezone

from .supervisor import Supervisor


class StoreAssociate(models.Model):
    name = models.CharField(max_length=50)
    supervisor = models.ForeignKey(Supervisor,
                                   related_name='employees',
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   blank=True)
    slot_start_time = models.DateTimeField(default=timezone.now)
    slot_end_time = models.DateTimeField(default=timezone.now)
    hourly_pay = models.DecimalField(decimal_places=2,
                                     max_digits=10,
                                     default=5)
    is_on_timeoff = models.BooleanField(default=False)
    is_checked_in = models.BooleanField(default=False)

    def __str__(self):
        return self.name
