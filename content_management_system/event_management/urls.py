from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path('events/<int:event_id>',views.events,name="events"),
    path('events/<int:event_id>/registration',views.registration,name="registration"),
    path('competition/<int:competition_id>',views.competition,name="competition"),
    path('competition/<int:competition_id>/competition_registration',views.competition_registration,name="competition_registration"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
]