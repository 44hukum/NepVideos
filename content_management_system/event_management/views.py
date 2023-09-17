from django.http.response import Http404, HttpResponse
from django.shortcuts import render

from .models import (
    Event,
    Competition,
    Look_and_feel,
    Booking,
    Competition_Registration as cr
)

from .Forms import Event_Registration,Competition_Registration

def index(request):
    look = Look_and_feel.objects.get(active_status = 'c')
    events = Event.objects.filter(event_status = 'upcomming') #GET EVENT OBJECT  
    competition = Competition.objects.all()
    return render(request,"event_management/index.html",{'events': events,'look': look,'competition':competition})  #SEND OBJECT

def events(request,event_id):
    # Get model
    if event_id:
        event = Event.objects.get(id = event_id)
        
        if events:
            form = Event_Registration()
            return render(request,"event_management/Register.html",{'event':event,'form':form})

    #query model
    #send result
    return Http404

def competition(request,competition_id):
    # Get model
    if competition_id:
        competition = Competition.objects.get(id = competition_id)
        
        if competition:
            form = Competition_Registration()
            return render(request,"event_management/competition.html",{'competition':competition,'form':form})

    #query model
    #send result
    return Http404

def registration(request,event_id):
    # Get model
    form = Event_Registration(request.POST)
    if event_id:
            event = Event.objects.get(id = event_id)
                    
            if form.is_valid():
                event_registration = Booking()
                event_registration.name = form.cleaned_data['name']
                event_registration.email = form.cleaned_data['email']
                event_registration.phonenumber = form.cleaned_data['phonenumber']
                event_registration.event = event
                
                event_registration.save()

                return render(request,"event_management/Register.html",{'event':event,'registration':True})
            return render(request,"event_management/Register.html",{'event':event,'validation_error':True})

    #query model
    #send result
    return Http404

def competition_registration(request,competition_id):
    # Get model
    form = Competition_Registration(request.POST)
    if competition_id:
            competition = Competition.objects.get(id = competition_id)
                    
            if form.is_valid():
                competition_registration = cr()
                competition_registration.name = form.cleaned_data['name']
                competition_registration.email = form.cleaned_data['email']
                competition_registration.phonenumber = form.cleaned_data['phonenumber']
                competition_registration.competition = competition
                
                competition_registration.save()
                print(competition_id)
                return render(request,"event_management/competition.html",{'competition':competition,'registration':True})
            return render(request,"event_management/competition.html",{'competition':competition,'validation_error':True})

    #query model
    #send result
    return Http404

