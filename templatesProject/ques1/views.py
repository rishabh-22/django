from django.shortcuts import render, HttpResponse

# Create your views here.
def order(request):

    person_name = "Rishabh"
    order_list = ['mobile', 'smart watch', 'earphones', 'sofa']
    warranty_flag = True

    return render(request, 'order.html', { 'person': person_name, 'order': order_list, 'warranty': warranty_flag} )
