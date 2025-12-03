from django.db import models
from django.utils import timezone

choice_user_types = [
    ('STUDENT', 'STUDENT'),
    ('PROFESSOR', 'PROFESSOR'),
    ('VISITOR', 'VISITOR'),
]


class SiteUser(models.Model):
    username = models.CharField(max_length=25, unique=True)
    user_type = models.CharField(max_length=16,
                                 choices=choice_user_types)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.username

    def _decrease_balance(self, amount: int):
        self.balance -= amount
        self.save()


class Article(models.Model):
    title = models.TextField()
    is_rentable = models.BooleanField(default=True)
    max_rent_days = models.IntegerField(default=7)
    rent_per_day = models.IntegerField(default=1)
    over_charge = models.IntegerField(default=2)
    price = models.IntegerField(default=25)
    count = models.IntegerField(default=1)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def _decrement_count(self):
        self.count -= 1
        if self.count == 0:
            self.is_available = False
        self.save()

    def _increment_count(self):
        self.count += 1
        self.is_available = True
        self.save()


class RentedItem(models.Model):
    user = models.ForeignKey(SiteUser,
                             on_delete=models.CASCADE,
                             related_name='rented_items')
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE,
                                related_name='rented_by')
    start_date = models.DateField(default=timezone.now)
    promised_end_date = models.DateField()
    actual_end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.article.title}: {self.user.username}'
