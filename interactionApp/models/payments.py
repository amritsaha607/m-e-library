from django.db import models
from django.utils import timezone

from .associate import StoreAssociate
from .supervisor import Supervisor

ALLOWED_DELAY = 1800


class AssociatePaymentAudit(models.Model):
    associate = models.ForeignKey(StoreAssociate,
                                  on_delete=models.CASCADE,
                                  related_name='payment_audits')
    amount = models.DecimalField(max_digits=10,
                                 decimal_places=2,
                                 default=0.00)
    date = models.DateField(default=timezone.now)
    check_in_time = models.DateTimeField(default=timezone.now)
    check_out_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def _compute_and_update_payment(self):
        associate = self.associate
        exp_check_in_time = associate.slot_start_time
        exp_check_out_time = associate.slot_end_time
        hourly_payment = associate.hourly_pay

        check_in_diff = self.check_in_time - exp_check_in_time
        check_out_diff = exp_check_out_time - self.check_out_time

        hours_worked = (self.check_out_time -
                        self.check_in_time).total_seconds / 3600
        self.amount = hours_worked * hourly_payment

        self.save()
