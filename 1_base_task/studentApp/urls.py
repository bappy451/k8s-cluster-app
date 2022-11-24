from django.urls import path
from studentApp.views import *

urlpatterns = [
    path('', first_view),
    # path('students/',StudentListView.as_view(), name='students')
]
