from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Publisher

# Create your views here.


class PublisherList(ListView):
    model = Publisher
    context_object_name = 'my_favorite_publishers'
    template_name = 'book_file.html'
    # queryset = Publisher.objects.all()
