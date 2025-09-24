from django.contrib import admin
from .models import Forklift, Battery, ChargeSession
admin.site.register(Forklift)
admin.site.register(Battery)
admin.site.register(ChargeSession)