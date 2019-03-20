from django.shortcuts import render, HttpResponse


# Create your views here.
def greet(request):
    name = "RISHABH"
    value = 9
    return render(request, 'index.html', {'name':name, 'value': value})