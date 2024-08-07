import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

GENRES = [
    'Action', 'Adventure', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Mystery', 
    'Romance', 'Sci-Fi', 'Slice of Life', 'Sports', 'Thriller'
]

def home(request):
    return render(request, 'home.html', {'genres': GENRES})

@csrf_exempt
def recommendations(request):
    selected_genres = request.POST.getlist('genres')
    recommendations = []
    for genre in selected_genres:
        response = requests.get(f'https://api.jikan.moe/v4/anime?genre={genre}')
        if response.status_code == 200:
            data = response.json()
            for anime in data['data']:
                recommendations.append({
                    'title': anime['title'],
                    'image_url': anime['images']['jpg']['image_url'],
                    'genre': genre,
                    'episodes': anime['episodes'],
                    'synopsis': anime['synopsis'],
                })
    return render(request, 'recommendations.html', {'recommendations': recommendations})
