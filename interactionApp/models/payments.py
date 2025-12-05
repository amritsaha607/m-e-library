from django.db import models
from django.utils import timezone

from .associate import StoreAssociate
from .supervisor import Supervisor


class AssociatePaymentAudit(models.Model):
    associate = models.ForeignKey(StoreAssociate,
                                  on_delete=models.CASCADE,
                                  related_name='payment_audits')
    amount = models.DecimalField(max_digits=10,
                                 decimal_places=2,
                                 default=0.00)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
