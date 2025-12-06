from django.http import JsonResponse
from django.views import View

from interactionApp.read_layer import fetch_associate_data
from interactionApp.utils import (_create_supervisor_change_request,
                                  _update_supervisor_change_request)


class RequestSupervisorChangeView(View):
    def post(self, request):
        associate_id = request.POST.get('associate_id')
        new_supervisor_id = request.POST.get('new_supervisor_id')
        data = _create_supervisor_change_request(
            associate_id, new_supervisor_id)
        return JsonResponse(data)


class UpdateSupervisorChangeRequestView(View):
    def post(self, request):
        supervisor_id = request.POST.get('supervisor_id')
        change_req_id = request.POST.get('change_req_id')
        new_status = request.POST.get('new_status')
        data = _update_supervisor_change_request(change_req_id,
                                                 supervisor_id,
                                                 new_status)
        return JsonResponse(data)
