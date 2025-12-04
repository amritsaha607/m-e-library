from django.contrib import admin

from .models import StoreAssociate, Supervisor, TimeOffRequest

admin.site.register([
    StoreAssociate,
    Supervisor,
    TimeOffRequest
])
