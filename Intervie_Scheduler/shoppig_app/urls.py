from django.urls import path
from .views import Add_Candidate_Slot,Add_Interviewer_Slot,Calculate_Slot
from . import views

urlpatterns=[
    path('candidate_slot',Add_Candidate_Slot.as_view()),
    path('interviewer_slot',Add_Interviewer_Slot.as_view()),
    path('calculate_slot',Calculate_Slot.as_view()),
]













































































