import requests
import collections


def search_movies(search_term):
    url = f'http://movie_service.talkpython.fm/api/search/{search_term}'
    resp = requests.get(url)

    MovieResult = collections.namedtuple(
        'MovieResult',
        'imdb_code, title, director, keywords, duration, genres, rating,'
        'year, imdb_score'
    )

    return [MovieResult(**me) for me in resp.json().get('hits')]
