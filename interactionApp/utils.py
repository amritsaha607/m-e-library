from django.utils import timezone

from .models import StoreAssociate, Supervisor, TimeOffRequest


def _get_associate_by_id(_id: str | int) -> StoreAssociate:
    return StoreAssociate.objects.get(id=_id)


def _get_supervisor_by_id(_id: str | int) -> Supervisor:
    return Supervisor.objects.get(id=_id)


def _get_timeoff_request_by_id(_id: str | int) -> TimeOffRequest:
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


def _approve_timeoff_request(timeoff_request: TimeOffRequest):
    timeoff_request.status = 'APPROVED'
    timeoff_request.save()


def _decline_timeoff_request(timeoff_request: TimeOffRequest):
    timeoff_request.status = 'DECLINED'
    timeoff_request.save()
