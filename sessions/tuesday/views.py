from django.shortcuts import render

# Create your views here.


def index(request):
    counter = request.session.get('counter', 0)
    counter = counter + 1
    request.session['counter'] = counter

    request.session.set_expiry(300)
    return render(request, 'index.html', {"count": counter})

