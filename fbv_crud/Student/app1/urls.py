from django.urls import path
from .views import StudentFormView,StudentDataView,StudentUpdateView,StudentDeleteView

urlpatterns=[
    path('student/',StudentFormView,name='studentForm'),
    path('studentData/',StudentDataView,name='studentData'),
    path('studentUpdate/<int:uid>/',StudentUpdateView,name='studentUpdate'),
    path('studentDelete/<int:did>/',StudentDeleteView,name='studentDelete')

]