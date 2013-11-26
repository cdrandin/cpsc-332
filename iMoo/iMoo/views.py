from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string

def display_root(request):
	return HttpResponse("iMoo Home page")