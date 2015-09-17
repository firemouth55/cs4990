from django.shortcuts import render
from django.views import generic

from .models import CaseStudy, Item


# Create your views here.

class IndexView(generic.ListView):
	template_name = 'caseStudy/index.html'
	model = CaseStudy
	#context_object_name = 'study'

class DetailView(generic.DetailView):
	model = CaseStudy
	template_name = 'casestudy/detail.html'
