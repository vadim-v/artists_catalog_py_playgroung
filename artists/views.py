from django.shortcuts import render

from django.http import HttpResponse


def index(request):
	return render(request, 'artists/index.html', {})

def add_artist(request):
	return render(request, 'artists/add.html', {})

def process_add_artist(request):
	print request.POST
	return HttpResponse('ok');
