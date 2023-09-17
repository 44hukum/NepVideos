from django.contrib import admin

from .models import Competition,Event,Booking,Competition_Registration,Look_and_feel

# Register your models here.
@admin.register(Competition_Registration)
class CompetitionRegistration(admin.ModelAdmin):
    list_display=('id','name','email','competition','phonenumber')


@admin.register(Booking)
class RegistrationAdmin(admin.ModelAdmin):
    list_display=('id','name','email','event','phonenumber')


@admin.register(Competition)
class Competition(admin.ModelAdmin):
    list_display=('id','name','competition_date','winner_price','runner_up_price','competition_registration_status')

@admin.register(Event)
class Event(admin.ModelAdmin):
    list_display=('id','event_name','event_date','event_description','event_status','event_registration_status')

@admin.register(Look_and_feel)
class LookAndFeel(admin.ModelAdmin):
    list_display = ('id','promo_event','quote_events_now','active_status')