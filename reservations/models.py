from django.db import models
#from django.utils import timezone
#from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Reservation(models.Model):
    REQUESTED = 1
    ACCEPTED = 2
    DENIED = 3
    STATUS = (
        (REQUESTED, "Requested"),
        (ACCEPTED, "Accepted"),
        (DENIED, "Denied"),
    )
    STOOL = 1
    WINDOW = 2
    SNUG = 3
    TABLE_TYPE = (
        (STOOL, "Bar Stool"),
        (WINDOW, "Window Seat"),
        (SNUG, "Snug"),
    )

    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    email = models.CharField(max_length=50, blank=False)
    date = models.DateField()
    seat_type = models.SmallIntegerField(choices=TABLE_TYPE, default=STOOL)
    reserved_start_time = models.TimeField()
    reserved_end_time = models.TimeField()
    status = models.SmallIntegerField(choices=STATUS, default=REQUESTED)

    def __str__(self):
        return "{0} for {1}  ({2} to {3})".format(
            self.status,
            self.date,
            self.reserved_start_time.strftime("%H:%M"),
            self.reserved_end_time.strftime("%H:%M"),
        )


class ReservationLineItem(models.Model):
    reservation = models.ForeignKey(Reservation, null=False)
    def __str__(self):
        return "{0} {1} {2}".format(
            self.reservation.full_name,
        self.reservation.seat_type, 
        self.reservation.reserved_start_time)

