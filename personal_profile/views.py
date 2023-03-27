from django.shortcuts import render
from django.views import generic



class Show_index(generic.TemplateView):
    template_name = 'personal_profile/index.html'

# Create your views here.
