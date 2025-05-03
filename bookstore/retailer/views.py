

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Retailer

class RetailerListView(ListView):
    model = Retailer
    template_name = 'retailer/retailer_list.html'
    context_object_name = 'retailer'

    def get_queryset(self):
        return Retailer.objects.filter(is_active=True)

class RetailerDetailView(DetailView):
    model = Retailer
    template_name = 'retailer/retailer_detail.html'
    context_object_name = 'retailer'

    def get_queryset(self):
        return Retailer.objects.filter(is_active=True)
