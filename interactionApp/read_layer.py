from .models import StoreAssociate
from .utils import _get_associate_by_id


def associate_to_json(associate: StoreAssociate):
    return {
        'name': associate.name,
        'supervisor': associate.supervisor.name,
        'slot_start_time': str(associate.slot_start_time),
        'slot_end_time': str(associate.slot_end_time),
        'hourly_pay': associate.hourly_pay,
    }


def fetch_associate_data(associate_id):
    """
    Check if associate is present in database
    """
    db_obj = _get_associate_by_id(associate_id)
    return associate_to_json(db_obj)
