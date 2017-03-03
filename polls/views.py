from django.shortcuts import render

def home(request):
	context = {}
	templates = 'home.html'
	return render(request, templates, context)
