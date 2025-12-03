from django.utils import timezone

from .models import Article, RentedItem, SiteUser


def _get_user_by_id(user_id: int) -> SiteUser:
    return SiteUser.objects.get(id=user_id)


def _get_article_by_id(user_id: int) -> Article:
    return Article.objects.get(id=user_id)


def _execute_article_rent_for_user(user_id: int, article_id: int, n_days: int):
    user = _get_user_by_id(user_id)
    article = _get_article_by_id(article_id)

    start_date = timezone.now()
    end_date = timezone.now() + timezone.timedelta(days=n_days)

    RentedItem.objects.create(
        user=user,
        article=article,
        start_date=start_date,
        promised_end_date=end_date,
    )

    total_rent_for_period = n_days * article.rent_per_day
    user._decrease_balance(total_rent_for_period)

    article._decrement_count()
