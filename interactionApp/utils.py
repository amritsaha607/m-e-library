from django.utils import timezone

from .models import (AssociatePaymentAudit, StoreAssociate, Supervisor,
                     SupervisorUpdateRequest, TimeOffRequest)

# This must be used across the codebase to parse dates
DATE_FORMAT = "%Y-%m-%d"

# This must be used across the codebase to parse datetime objects
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


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


def _log_associate_check_in(associate_id, check_in_time):
    associate = _get_associate_by_id(associate_id)
    AssociatePaymentAudit.objects.create(
        associate=associate,
        date=timezone.now(),
        check_in_time=check_in_time,
    )


def _log_associate_check_out(associate_id, check_out_time):
    associate = _get_associate_by_id(associate_id)
    audit = AssociatePaymentAudit.objects.get(
        associate=associate,
        date=timezone.now(),
    )
    audit.check_out_time = check_out_time
    audit.save()


def _update_associate_payment(associate_id):
    associate = _get_associate_by_id(associate_id)
    audit = AssociatePaymentAudit.objects.get(
        associate=associate,
        date=timezone.now(),
    )

    audit._compute_and_update_payment()


def _create_supervisor_change_request(associate_id, new_supervisor_id):
    associate = _get_associate_by_id(associate_id)
    cur_supervisor = associate.supervisor
    new_supervisor = _get_supervisor_by_id(new_supervisor_id)

    return SupervisorUpdateRequest.objects.create(
        raised_by=associate,
        new_supervisor=new_supervisor,
    )
