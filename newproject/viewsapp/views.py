from django.shortcuts import render, HttpResponse

# Create your views here.

# homepage
def index(request):
	# print(request)
	return render(request, 'index.html')
def second(request, ids):
	# return HttpResponse(ids)
	if (ids > 6 and ids < 12):
		return HttpResponse("Good morning")
	if (ids > 12 and ids < 18):
		return HttpResponse("Good afternoon")
	if (ids > 18 and ids < 24):
		return HttpResponse("Good night")
	else:
		return HttpResponse("Go to bed")
