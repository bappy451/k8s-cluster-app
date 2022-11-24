from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Create your views here.
def first_view(request):
    return HttpResponse("<h1>Django is cool and Docker Volumes are super awesome</h1>")