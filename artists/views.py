import urllib, json
from django.shortcuts import render

from django.http import HttpResponse

from .models import Artist, Album


def index(request):
  return render(request, 'artists/index.html', {})

def browse_artist(request):
  artists = Artist.objects.all()
  return render(request, 'artists/browse.html', { 'artists': artists })

def fetch_albums(request, artist_id):
  artist = Artist.objects.get(id=artist_id)
  albums = artist.album_set.all()
  return render(request, 'artists/albums.html', { 'albums': albums })

def add_artist(request):
  return render(request, 'artists/add.html', {})


def process_add_artist(request):
  artist_name = request.POST.get('name')

  try:
    url = "https://itunes.apple.com/search?term=" + urllib.quote_plus(artist_name) + "&media=music&entity=album"
    response = urllib.urlopen(url)
    albums_data = json.loads(response.read())

    if albums_data.get('resultCount') > 0:
      artist = Artist(name=artist_name)
      artist.save()

      for result in albums_data.get('results'):
        artist.album_set.create(name=result['collectionName'], image_url=result['artworkUrl100'], release_date=result['releaseDate'])

    else:
      return HttpResponse('err')

  except:
    return HttpResponse('err')

  else:
    return HttpResponse('ok')
