from django.db import models
from django.utils import timezone

choice_user_types = [
    ('BOT', 'BOT'),
    ('USER', 'USER'),
    ('CELEBRITY', 'CELEBRITY'),
]


class SiteUser(models.Model):
    username = models.CharField(max_length=25, unique=True)
    user_type = models.CharField(max_length=16,
                                 choices=choice_user_types)
    is_approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=timezone.now)

    followers = models.ManyToManyField('SiteUser',
                                       related_name='following')
    friend_requests = models.ManyToManyField('SiteUser',
                                             related_name='sent_requests')

    def __str__(self):
        return self.username
