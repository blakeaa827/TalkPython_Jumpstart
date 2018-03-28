import os
import requests
import subprocess
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
    return dir_path


def get_lolcat(dir_path):
    r = requests.get('http://www.lolcats.com')
    soup: BeautifulSoup = BeautifulSoup(r.text, 'html.parser')
    for line in soup.findAll(class_='lolcat'):
        img_url = 'http://www.lolcats.com' + line.get('src')
        file_name = img_url.split('/')[-1]
        img_response = requests.get(img_url)
        img = img_response.content
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, 'wb') as img_file:
            img_file.write(img)


def open_lolcat(dir_path):
    subprocess.Popen(f'explorer "{dir_path}"')


def main():
    dir_name = 'lolcats'

    print_header()
    dir_path = get_dir(dir_name)
    get_lolcat(dir_path)
    open_lolcat(dir_path)


if __name__ == '__main__':
    main()
