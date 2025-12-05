from django.utils import timezone

from interactionApp.models import AssociatePaymentAudit
from interactionApp.utils import _log_associate_check_in


def store_check_in(request):
    """
    Validates incoming request parameters' data types.
    Checks if the related objects exists in the system/database.
    Should validate if a payment audit already exists for the day for this associate.
    """

    associate_id = request.POST['associate_id']
    check_in_time = request.POST['check_in_time']
    _log_associate_check_in(associate_id, check_in_time)
