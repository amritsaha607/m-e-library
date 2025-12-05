from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from interactionApp.models import AssociatePaymentAudit
from interactionApp.responses import (RESPONSE_CONFLICT, RESPONSE_OK,
                                      RESPONSE_UNAUTHORIZED)
from interactionApp.utils import (_approve_timeoff_request,
                                  _create_timeoff_request,
                                  _decline_timeoff_request,
                                  _get_associate_by_id,
                                  _get_timeoff_request_by_id,
                                  _log_associate_check_in,
                                  _log_associate_check_out,
                                  _update_associate_payment)


@csrf_exempt
def store_check_in(request):
    """
    Validates incoming request parameters' data types.
    Checks if the related objects exists in the system/database.
    Should validate if a payment audit already exists for the day for this associate.
    """

    associate_id = request.POST['associate_id']
    check_in_time = request.POST['check_in_time']
    _log_associate_check_in(associate_id, check_in_time)
    return JsonResponse(RESPONSE_OK)


@csrf_exempt
def store_check_out(request):
    """
    Validates incoming request parameters' data types.
    Checks if the related objects exists in the system/database.
    Should validate if no payment audit is present for this scenario.
    """

    associate_id = request.POST['associate_id']
    check_out_time = request.POST['check_out_time']
    _log_associate_check_out(associate_id, check_out_time)
    return JsonResponse(RESPONSE_OK)


@csrf_exempt
def update_associate_payment(request):
    """
    Validates incoming request parameters' data types.
    Checks if the related objects exists in the system/database.
    Should validate logical flows and edge cases.
    """

    associate_id = request.POST['associate_id']
    _update_associate_payment(associate_id)
    return JsonResponse(RESPONSE_OK)
