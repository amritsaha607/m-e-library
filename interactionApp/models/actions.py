from django.db import models
from django.utils import timezone

from .associate import StoreAssociate
from .supervisor import Supervisor


class ExceptionRequest(models.Model):
    raised_at = models.DateTimeField(default=timezone.now)
    raised_by = models.ForeignKey(StoreAssociate,
                                  related_name='raised_exceptions',
                                  on_delete=models.CASCADE)
    approval_requested_by = models.ForeignKey(Supervisor,
                                              related_name='exception_requests',
                                              on_delete=models.SET_NULL,
                                              null=True,
                                              blank=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.raised_by)
