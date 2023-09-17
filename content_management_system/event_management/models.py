from django.db import models

# models to manage events
class Event(models.Model):
    EVENT_CHOICE = (
        ('upcomming','upcomming'),
        ('completed',"completed"),
    )

    REGISTRATION_STATUS =(
        ('open','open'),
        ('closed','closed'),
        ('notopen','notopen ')
    )

    event_name = models.CharField(max_length=200)
    event_date = models.DateTimeField()
    feature_image = models.FileField(upload_to="events")
    event_description = models.TextField()
    event_status = models.CharField(max_length=12,choices=EVENT_CHOICE,default=EVENT_CHOICE[0][0])
    event_registration_status = models.CharField(max_length=10,choices=REGISTRATION_STATUS,default=REGISTRATION_STATUS[0][0])
    
    def __str__(self) -> str:
        return self.event_name

    class Meta:
        ordering = ('-event_date',)


class Booking(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.name


class Competition(models.Model):
    REGISTRATION_STATUS =(
        ('open','open'),
        ('closed','closed'),
        ('notopen','notopen ')
    )

    name = models.CharField(max_length=200)
    competition_date = models.DateTimeField()
    feature_image = models.ImageField(upload_to = "Competitions")
    competition_description = models.TextField()
    winner_price = models.CharField(max_length=100)
    runner_up_price = models.CharField(max_length=100)
    competition_registration_status = models.CharField(max_length=10,choices=REGISTRATION_STATUS,default=REGISTRATION_STATUS[0][0])

    def __str__(self) -> str:
        return self.name


class Competition_Registration(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.name

class Look_and_feel(models.Model):
    ACTIVE_CHOICE =(
        ('c','current'),
        ('o','off')
    )

    feature_image = models.ImageField(upload_to = "home")
    promo_event = models.ForeignKey(Event,null=True,on_delete=models.CASCADE, related_name="events")
    about_events_now = models.TextField()
    quote_events_now = models.CharField(max_length=200)
    active_status = models.CharField(max_length=1,choices=ACTIVE_CHOICE,default=ACTIVE_CHOICE[1][0])

    class Meta:
        db_table = 'Herald Event Manager'

    def __str__(self) -> str:
        return "{0} {1}".format("Herald Event Manager",self.active_status)