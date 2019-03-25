from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.views import View
import datetime

#
 Create your views here.

def home(request):
	now = datetime.datetime.now()
	hr = now.hour
	
	if(hr>=5 and hr<12):
		message = "Good Morning"
	elif (hr>=12 and hr<17):
		message = "Good Afternoon"
	elif (hr>=17 and hr<21):
		message = "Good Evening"
	elif (hr >=21 and hr<24):
		message = "Good Night"
	else:
		message = "IDK what to say! go to bed."
		
	return message
