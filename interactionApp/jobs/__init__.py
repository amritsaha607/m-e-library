from django.utils import timezone

from interactionApp.models import StoreAssociate, TimeOffRequest


def clear_existing_timeoffs():
    """
    Resets the timeoff attribute of all the associates having timeoff flag on
    """
    StoreAssociate.objects.filter(
        is_on_timeoff=True).update(is_on_timeoff=False)


def populate_timeoffs():
    """
    Populates the timeoff attribute of store associates based on approved requests
    """
    current_date = timezone.now()
    approved_timeoff_requests_for_today = TimeOffRequest.objects.filter(
        request_date=current_date.date,
        status='APPROVED',
    )
    for timeoff_req in approved_timeoff_requests_for_today:
        associate = timeoff_req.approval_requested_by
        associate.is_on_timeoff = True
        associate.save()


def timeoff_population_job():
    clear_existing_timeoffs()
    populate_timeoffs()
