from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from interactionApp.responses import RESPONSE_OK, RESPONSE_UNAUTHORIZED
from interactionApp.utils import _create_timeoff_request, _get_associate_by_id


@csrf_exempt
def request_timeoff(request):
    requesting_user_id = request.POST['user_id']
    request_date = request.POST['exception_date']

    associate = _get_associate_by_id(requesting_user_id)
    _create_timeoff_request(associate, associate.supervisor, request_date)

    return JsonResponse(RESPONSE_OK)
