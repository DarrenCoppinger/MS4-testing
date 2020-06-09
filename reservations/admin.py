from django.contrib import admin
from .models import Reservation

# Register your models here.

# class ReservationLineAdminInLine(admin.TabularInline):
#     model = Reservation


admin.site.register(Reservation)
