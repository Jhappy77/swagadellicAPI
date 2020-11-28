from django.contrib import admin
from .models import *

admin.site.register(Movie)
admin.site.register(Theatre)
admin.site.register(Screening)
admin.site.register(RegisteredUser)
admin.site.register(Ticket)
admin.site.register(Payment)
admin.site.register(PaymentForTicket)
admin.site.register(SavedDebit)
admin.site.register(SavedCredit)

