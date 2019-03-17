from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
import datetime

# Create your views here.

def home(request):
	# return HttpResponse('Hello World!')
	now = datetime.datetime.now()
	hr = now.hour
	print (hr)
	# return HttpResponse(hr)
	if(hr>=5 and hr<12):
		return HttpResponse("Good Morning")
	if (hr>=12 and hr<17):
		return HttpResponse("Good Afternoon")
	if (hr>=17 and hr<21):
		return HttpResponse("Good Evening")
	if (hr >=21 and hr<=1):
		return HttpResponse("Good Night")
	else:
		return HttpResponse("IDK what to say! go to bed.")
