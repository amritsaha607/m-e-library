from django.http import JsonResponse

from .responses import RESPONSE_OK, RESPONSE_UNAUTHORIZED
from .utils import (_add_friend_request, _add_user_to_session, _follow_user,
                    get_user_by_id)


def request_friendship(request):
    req_user_id = request.GET['requestor']
    sent_user_id = request.GET['user']

    req_user = get_user_by_id(req_user_id)
    sent_user = get_user_by_id(sent_user_id)

    _add_friend_request(requestor=req_user,
                        sent_to=sent_user)

    return JsonResponse(RESPONSE_OK)


def follow_user(request):
    req_user_id = request.GET['requestor']
    sent_user_id = request.GET['user']

    req_user = get_user_by_id(req_user_id)
    sent_user = get_user_by_id(sent_user_id)

    _follow_user(req_user, sent_user)

    return JsonResponse(RESPONSE_OK)


def login(request):
    user_id = request.POST['user_id']
    _add_user_to_session(user_id)
    return JsonResponse(RESPONSE_OK)
