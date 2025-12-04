from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from interactionApp.responses import RESPONSE_OK, RESPONSE_UNAUTHORIZED
from interactionApp.utils import (_approve_timeoff_request,
                                  _create_timeoff_request,
                                  _get_associate_by_id,
                                  _get_timeoff_request_by_id)


@csrf_exempt
def request_timeoff(request):
    requesting_user_id = request.POST['user_id']
    request_date = request.POST['exception_date']

    associate = _get_associate_by_id(requesting_user_id)
    _create_timeoff_request(associate, associate.supervisor, request_date)

    return JsonResponse(RESPONSE_OK)


@csrf_exempt
def approve_timeoff_request(request):
    approver_id = request.POST['approver_id']
    timeoff_request_id = request.POST['timeoff_request_id']

    timeoff_request = _get_timeoff_request_by_id(timeoff_request_id)
    _approve_timeoff_request(timeoff_request)

    return JsonResponse(RESPONSE_OK)
