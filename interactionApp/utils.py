from .models import SiteUser


def get_user_by_id(user_id: str):
    return SiteUser.objects.get(id=user_id)


def add_friend_request(requestor: SiteUser, sent_to: SiteUser):
    sent_to.friend_requests.add(requestor)
    sent_to.save()


def follow_user(following: SiteUser, follower: SiteUser):
    follower.followers.add(following)
    follower.save()
