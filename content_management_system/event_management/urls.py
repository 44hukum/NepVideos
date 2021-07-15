from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path('events/<int:event_id>',views.events,name="events"),
    path('competition/<int:event_id>',views.competition,name="competition"),
    path('events/<int:event_id>/registration',views.registration,name="registration")
]