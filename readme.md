#### GET Associate API

- Reads associate data from cache, if present returns data from cache
- If not found in cache, reads from database
- Updates the cache with associate data in an asynchronous thread
- Returns associate data

We're using Azure Redis cache for this implementation. Any implementation being done must support Azure Redis cache. A ttl should be set to every cache item with a max life of 1 day. We can assume we have enough storage in cache and storing data is not a challenge.
If associate data is not present in database & cache, it MUST return with 404 response code.

#### Features

- StoreAssociate can check in and check out in the store. When an associate checks in the store, associate will be marked as checked in (is_checked_in attribute will be updated to True). When checked out, the flag will go false.
- For the first checkin of the day, if the associate is more late than 30 minutes from the slot_start_time, a prorated loss of pay will be incurred for the day based on number of minutes of delay from the slot_start_time.
- For the last checkout of the day, if the associate checks out earlier than 30 minutes of slot_end_time, a prorated loss of pay will be incurred for the day based on number of minutes.
- However, an associate can request a timeoff, and the immediate supervisor can approve the timeoff request which will be valid for a particular day. If an associate has an approved timeoff for a day, loss of pay will not be incurred for that associate. This is a special use case.
- A StoreAssociate can only raise one timeoff request for a particular date. However, there is no restriction on how much request user can raise in a timeframe as long as they are for different days. It can be assumed that a user slot_start_time and slot_end_time falls under the same day with respect to the server timezone.
- Supervisors can approve timeoff requests raised by StoreAssociates which belongs to their approval category. A supervisor cannot approve another supervisor's approval request.
- Once a timeoff request is approved/declined, no modification can be made to that specific request, even by Supervisors.
