from django.http import JsonResponse

from .responses import RESPONSE_OK, RESPONSE_UNAUTHORIZED
from .utils import _execute_article_rent_for_user


def rent_article(request):
    user_id = request.POST['user_id']
    article_id = request.POST['article_id']
    n_days = request.POST['requested_days']

    _execute_article_rent_for_user(user_id, article_id, n_days)

    return JsonResponse(RESPONSE_OK)
