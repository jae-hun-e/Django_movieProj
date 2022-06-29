from django.shortcuts import render
import requests
import json
from .froms import SearchForm

my_id = 'e3ffb6091393154ff4a81caaf0b29666'


def home(req):
    if req.method == "POST":
        form = SearchForm(req.POST)
        searchword = req.POST.get('search')
        if form.is_valid():
            url = 'https://api.themoviedb.org/3/search/movie?api_key=' + my_id + '&query=' + searchword
            responce = requests.get(url)
            resdata = responce.text
            obj = json.loads(resdata)
            obj = obj['results']
            return render(req, 'search.html', {'obj': obj})
    else:
        form = SearchForm()
        url = 'https://api.themoviedb.org/3/trending/all/day?api_key=' + my_id
        responce = requests.get(url)
        resdata = responce.text
        obj = json.loads(resdata)
        obj = obj['results']
    return render(req, 'index.html', {'obj': obj, 'form': form})


def detail(req, movie_id):
    url = 'https://api.themoviedb.org/3/movie/' + movie_id + '?api_key=' + my_id
    responce = requests.get(url)
    resdata = responce.text
    resdata = json.loads(resdata)
    return render(req, 'detail.html', {'resdata': resdata})
