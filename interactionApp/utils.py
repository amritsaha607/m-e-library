from django.utils import timezone

from .models import StoreAssociate, Supervisor, TimeOffRequest


def _get_associate_by_id(_id: str | int):
    return StoreAssociate.objects.get(id=_id)


def _get_supervisor_by_id(_id: str | int):
    return Supervisor.objects.get(id=_id)


def _get_timeoff_request_by_id(_id: str | int):
    return TimeOffRequest.objects.get(id=_id)


def _create_timeoff_request(associate: StoreAssociate,
                            supervisor: Supervisor,
                            request_date: str) -> TimeOffRequest:
    cur_timestamp = timezone.now()
    return TimeOffRequest.objects.create(
        raised_at=cur_timestamp,
        request_date=request_date,
        raised_by=associate,
        approval_requested_by=supervisor,
        is_approved=False,
    )
