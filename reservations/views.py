from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import ReservationForm
from .models import ReservationLineItem
from django.conf import settings
from django.utils import timezone
# from products.models import Product

# Create your views here.

@login_required()
def reservation(request):
    if request.method == "POST":
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)

            reservation.save()
            messages.error(
                request, "Your have requested a booking. A member of our staff will be in touch shortly to confirm your booking."
                )
            return redirect(reverse('index'))
        else:
            print(reservation_form.errors)
            messages.error(request, "We were unable to make this reservation")
    else:
        reservation_form = ReservationForm()

    return render(
        request,
        "reservation.html",
        {'reservation_form': reservation_form}
        )

