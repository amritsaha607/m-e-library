from django.http import JsonResponse
from django.views import View

from interactionApp.responses import (RESPONSE_CONFLICT, RESPONSE_OK,
                                      RESPONSE_UNAUTHORIZED)
from interactionApp.utils import (_create_supervisor_change_request,
                                  _update_supervisor_change_request)


class RequestSupervisorChangeView(View):
    def post(self, request):
        """
        Make sure associate_id and new_supervisor_id are positive integers.
        Must check if the corresponding objects are available in the database. If not, raise BAD_REQUEST.
        """
        associate_id = request.POST.get('associate_id')
        new_supervisor_id = request.POST.get('new_supervisor_id')
        _create_supervisor_change_request(
            associate_id, new_supervisor_id)
        return JsonResponse(RESPONSE_OK)


class UpdateSupervisorChangeRequestView(View):
    def post(self, request):
        """
        Make sure supervisor_id and change_req_id are positive integers
        and new_status belongs to one of the status choices, it cannot be PENDING.
        Must check if the corresponding objects are available in the database. If not, raise BAD_REQUEST.
        """
        supervisor_id = request.POST.get('supervisor_id')
        change_req_id = request.POST.get('change_req_id')
        new_status = request.POST.get('new_status')
        _update_supervisor_change_request(change_req_id,
                                          supervisor_id,
                                          new_status)
        return JsonResponse(RESPONSE_OK)
