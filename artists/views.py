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

  template = 'artists/albums.html'
  page_template = 'artists/albums_entries.html'

  if request.is_ajax() and request.POST.get('pagination') is None:
    template = page_template

  if request.GET.get('order') == 'asc':
    albums = artist.album_set.order_by('release_date')
  else:
    albums = artist.album_set.all()

  return render(request, template, { 'albums': albums, 'artist_id': artist_id, 'page_template': page_template })

def search_albums(request):
  artist_id = request.POST.get('artist_id')
  artist = Artist.objects.get(id=artist_id)

  template = 'artists/albums.html'
  page_template = 'artists/albums_entries.html'
  if request.is_ajax() and request.POST.get('pagination') is None:
    template = page_template


  search_term = request.POST.get('term')
  albums = artist.album_set.filter(name__contains=search_term)

  return render(request, template, {'albums': albums, 'artist_id': artist_id, 'page_template': page_template})

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
