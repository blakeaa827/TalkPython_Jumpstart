from movie_svc import search_movies
import requests

def main():
    print_banner()
    while True:
        search_for = input('For what movies should I search? (or E[x]it) ')
        if search_for == 'x':
            print('Good Bye!!!')
            exit(0)
        else:
            try:
                movies = sorted(get_movies(search_for), key=lambda m: -m.year)
                for m in movies:
                    print(f'{m.year} -- {m.title}')
                print()
            except ValueError:
                print("ValueError: a search term must be provided")
            except requests.exceptions.ConnectionError:
                print("ConnectionError: cannot establish connection to search "
                      "server")
            except Exception as ge:
                print(f"UnexpectedError: {ge}")


def print_banner():
    print('-----------------------------------')
    print('        MOVIE SEARCH APP')
    print('-----------------------------------')
    print('\n')


def get_movies(search_for):
    return search_movies(search_for)


if __name__ == '__main__':
    main()
