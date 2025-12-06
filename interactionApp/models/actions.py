from django.db import models
from django.utils import timezone

from ._utils import STATUS_CHOICES
from .associate import StoreAssociate
from .supervisor import Supervisor


class TimeOffRequest(models.Model):
    raised_at = models.DateTimeField(default=timezone.now)
    request_date = models.DateField()
    raised_by = models.ForeignKey(StoreAssociate,
                                  related_name='raised_exceptions',
                                  on_delete=models.CASCADE)
    approval_requested_by = models.ForeignKey(Supervisor,
                                              related_name='exception_requests',
                                              on_delete=models.SET_NULL,
                                              null=True,
                                              blank=True)
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=10,
                              default='PENDING')

    def __str__(self):
        return str(self.raised_by)
