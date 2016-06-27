import urllib, json
from django.shortcuts import render

from django.http import HttpResponse

from .models import Artist, Album


def index(request):
	return render(request, 'artists/index.html', {})

def add_artist(request):
	return render(request, 'artists/add.html', {})

def process_add_artist(request):
	artist_name = request.POST.get('name')
	url         = "https://itunes.apple.com/search?term=" + urllib.quote_plus(artist_name) +"&media=music&entity=album"
	response    = urllib.urlopen(url)
	albums_data = json.loads(response.read())

	artist = Artist(name=artist_name)
	artist.save()

	for result in albums_data.get('results'):
		artist.album_set.create(name=result['collectionName'], image_url=result['artworkUrl100'])

	return HttpResponse('ok');
