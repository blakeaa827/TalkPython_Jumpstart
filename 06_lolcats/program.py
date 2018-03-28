import os
import requests
from bs4 import BeautifulSoup


def print_header():
    print('-------------------------------')
    print('    LOL CAT FACTORY APP')
    print('-------------------------------')
    print('\n')


def get_dir(name):
    dir_path = os.path.join('.', name)
    if not os.path.isdir(dir_path):
        print(f'Could not find {dir_path}.  Creating it now.')
        os.mkdir(dir_path)
    else:
        print(f'Found {dir_path}.  Using existing location.')


def get_lolcat():
    r = requests.get('http://www.lolcats.com')
    soup: BeautifulSoup = BeautifulSoup(r.text, 'html.parser')
    print(soup.find(class_='lolcat'))


def main():
    dir_name = 'lolcats'

    print_header()
    get_dir(dir_name)
    get_lolcat()


if __name__ == '__main__':
    main()
