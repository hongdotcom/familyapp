from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from .models import familyevent,eventsupply

def home(request):
  events = familyevent.objects.all()
 
  return render(request, 'home.html', {'events': events})

def event_details(request, pk):
    event = get_object_or_404(familyevent, pk=pk)
    supply = eventsupply.objects.filter(event=pk)
    return render(request, 'event_details.html', {'supply': supply,'event': event})