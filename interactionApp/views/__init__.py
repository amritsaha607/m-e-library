import schedule

from interactionApp.jobs import timeoff_population_job

from .activity import store_check_in, store_check_out
from .leaves import (approve_timeoff_request, decline_timeoff_request,
                     request_timeoff)
from .lookup import AssociateLookupView

schedule.every().day.at("00:00").do(timeoff_population_job)
