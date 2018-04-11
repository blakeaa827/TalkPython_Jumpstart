from movie_svc import search_movies

def main():
    print_banner()

    movies = sorted(get_movies(), key=lambda m: -m.year)
    for m in movies:
        print(f'{m.year} -- {m.title}')


def print_banner():
    print('-----------------------------------')
    print('        MOVIE SEARCH APP')
    print('-----------------------------------')
    print('\n')


def get_movies():
    search_for = input('For what movies should I search? (or E[x]it) ')
    if search_for == 'x':
        print('Good Bye!!!')
        exit(0)
    else:
        return search_movies(search_for)


if __name__ == '__main__':
    main()
