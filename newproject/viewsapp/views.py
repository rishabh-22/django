from django.shortcuts import render, HttpResponse

# Create your views here.

# homepage
def index(request):
	# print(request)
	return render(request, 'index.html')
def second(request, ids):
	
	if ids >= 6 and ids < 12:
		message = "Good morning!"
	elif ids >= 12 and ids < 18:
		message = "Good afternoon"
	elif ids >= 18 and ids < 24:
		message ="Good night"
	else:
		# return HttpResponse("Go to bed")
		message = "Go to bed"
	return HttpResponse(message)


def methodForTest(request, ids):
	
	if ids >= 6 and ids < 12:
		message = "Good morning!"
	elif ids >= 12 and ids < 18:
		message = "Good afternoon"
	elif ids >= 18 and ids < 24:
		message ="Good night"
	else:
		message = "Go to bed"
	return message

