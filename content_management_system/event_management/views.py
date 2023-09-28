from django.http.response import Http404, HttpResponse
from django.shortcuts import render
# accounts/views.py
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .Forms import CustomUserCreationForm, CustomAuthenticationForm

from .models import (
    Event,
    Competition,
    Look_and_feel,
    Booking,
    Competition_Registration as cr
)

from .Forms import CreatorBooking,Competition_Registration

@login_required
def index(request):
    look = Look_and_feel.objects.get(active_status = 'c')
    events = Event.objects.filter(event_status = 'upcomming') #GET EVENT OBJECT  
    competition = Competition.objects.all()
    return render(request,"event_management/index.html",{'events': events,'look': look,'competition':competition})  #SEND OBJECT

@login_required
def events(request,event_id):
    # Get model
    if event_id:
        event = Event.objects.get(id = event_id)
        
        if events:
            form = CreatorBooking()
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

@login_required
def registration(request,event_id):
    # Get model
    form = CreatorBooking(request.POST)
    if event_id:
            booking = Event.objects.get(id = event_id)
                    
            if form.is_valid():
                book_creator = Booking()
                book_creator.name = form.cleaned_data['name']
                book_creator.email = form.cleaned_data['email']
                book_creator.phonenumber = form.cleaned_data['phonenumber']
                book_creator.event = booking
                
                book_creator.save()

                return render(request,"event_management/Register.html",{'event':booking,'registration':True})
            return render(request,"event_management/Register.html",{'event':booking,'validation_error':True})

    #query model
    #send result
    return Http404

@login_required
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




def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Change 'dashboard' to your desired success URL
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Change 'dashboard' to your desired success URL
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def dashboard(request):
    # Your dashboard view logic here
    return render(request, 'dashboard.html')
