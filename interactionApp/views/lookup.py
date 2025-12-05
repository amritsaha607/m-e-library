from django.http import JsonResponse
from django.views import View

from interactionApp.read_layer import fetch_associate_data


class AssociateLookupView(View):
    def get(self, request):
        associate_id = request.GET.get('associate_id')
        data = fetch_associate_data(associate_id)
        return JsonResponse(data)
