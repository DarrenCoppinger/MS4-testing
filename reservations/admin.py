from django.contrib import admin
from .models import Reservation
from .form import ReservationForm
from django.core.mail import send_mail
from django.conf import settings
# Register your models here.


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date', 'status')
    # add_form = ReservationForm()
    readonly_fields = ('full_name', 'phone_number', 'email')
    print('ReservationAdmin')

    def save_model(self, request, obj, form, change):
        if change:
            print('Inside check loop 1')
            print(obj)
            if(obj.status == 2):
                subject = "Status Changed - ACCEPTED"
                message = "Status Changed - ACCEPTED"
            elif(obj.status == 3):
                subject = "Status Changed - DENIED"
                message = "Status Changed - DENIED"
            # print('request.email ' + str(request.email))
            # subject = "Status Changed"
            # message = "Status Changed"
            from_email = settings.EMAIL_HOST_USER
            to_list = [obj.email, settings.EMAIL_HOST_USER]
            send_mail(
                subject,
                message,
                from_email,
                to_list,
                fail_silently=False)
        return super().save_model(request, obj, form, change)

admin.site.register(Reservation, ReservationAdmin)


    # reservation_form = ReservationForm(request.POST)
    # if reservation_form.is_valid():
    #     reservation = reservation_form.save(commit=False)
    #     reservation.save()


    # def save_formset(self, request, form, formset, change):
    #     if change:
    #         print('Inside check loop')
    #     return super().save_formset(request, form, formset, change)


    # def save_
    #     # print('ReservationAdmin')
    #     initial_reservation_form = ReservationForm(request.POST)
    #     initial_reservation_status = initial_reservation_form.status

    #     reservation = reservation_form.save(commit=False)
    #     Current_reservation_status = reservation.status

    #     check = ReservationForm(request.POST, initial=initial_reservation_form)

    #     print('email=' + str(reservation_form.email))
    #     if check.has_changed():
    #         print('Inside check loop')
 
    #         super().save_formset(self, request, form, formset, change)


        #    subject = "Status Changed"
        #     message = "Status Changed"
        #     from_email = settings.EMAIL_HOST_USER
        #     to_list = [self.email, settings.EMAIL_HOST_USER]
        #     send_mail(
        #         subject,
        #         message,
        #         from_email,
        #         to_list,
        #         fail_silently=False)


# class ReservationLineAdminInLine(admin.TabularInline):
#     model = Reservation

# class ReservationInLine(admin.TabularInline):
#     models = Reservation

# @admin.register(Account)
# class AccountAdmin(UserAdmin):
#     inlines = (ApplicationInLine,)


# class ReservationInLine(admin.TabularInline):
#     model = Reservation

    # inlines = (ReservationInLine,)

    # def save_formset(self, request, form, formset, change):
    #     reservation_form = ReservationForm(request.POST)
    #     reservation = reservation_form.save(commit=False)
    #     reservation.save()
    #     if formset.has_changed():
    #         super().save_formset(request, reservation_form, formset, change)

    #         subject = "Status Changed"
    #         message = "Status Changed"
    #         from_email = settings.EMAIL_HOST_USER
    #         to_list = [reservation.email, settings.EMAIL_HOST_USER]
    #         send_mail(subject, message, from_email, to_list, fail_silently=False)
