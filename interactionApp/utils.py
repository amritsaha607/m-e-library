from .models import SiteUser


def get_user_by_id(user_id: str):
    return SiteUser.objects.get(id=user_id)


def _add_friend_request(requestor: SiteUser, sent_to: SiteUser):
    sent_to.friend_requests.add(requestor)
    sent_to.save()


def _follow_user(following: SiteUser, follower: SiteUser):
    follower.followers.add(following)
    follower.save()


def _add_user_to_session(request, user_id: int):
    request.session['user_id'] = user_id
