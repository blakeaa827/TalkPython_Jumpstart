import requests
import collections


def search_movies(search_term):
    search = search_term
    url = f'http://movie_service.talkpython.fm/api/search/{search}'

    resp = requests.get(url)
    resp_json: dict = resp.json()
    movie_list = resp_json.get('hits')

    MovieResult = collections.namedtuple(
        'MovieResult',
        'imdb_code, title, director, keywords, duration, genres, rating,'
        'year, imdb_score'
    )

    return [MovieResult(**me) for me in movie_list]
