import os
import platform
import requests
import shutil
import subprocess
from bs4 import BeautifulSoup


def print_header():
    print('-------------------------------')
    print('    LOL CAT FACTORY APP')
    print('-------------------------------')
    print('\n')


def get_dir(name):
    dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), name))
    if not os.path.isdir(dir_path):
        print(f'Could not find {dir_path}.  Creating it now.')
        os.mkdir(dir_path)
    else:
        print(f'Found {dir_path}.  Using existing location.')
    return dir_path


def get_lolcat(dir_path):
    r = requests.get('http://www.lolcats.com/gallery/new.html')
    soup: BeautifulSoup = BeautifulSoup(r.text, 'html.parser')
    for line in soup.findAll(class_='gallery-item')[:10]:
        img_page_url = 'http://www.lolcats.com' + line.a.get('href')
        r = requests.get(img_page_url)
        img_soup = BeautifulSoup(r.text, 'html.parser')
        img_url = 'http://www.lolcats.com' + img_soup.find(class_='lolcat').get('src')
        img = requests.get(img_url, stream=True).raw
        file_name = img_url.split('/')[-1]
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, 'wb') as fout:
            print(f'copying file {file_name}')
            shutil.copyfileobj(img, fout)


def open_lolcat(dir_path):
    if platform.system() == 'Windows':
        subprocess.call(['explorer', dir_path])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', dir_path])
    elif platform.system() == 'Darwin':
        subprocess.call(['open', dir_path])
    else:
        print(f'Sorry, we don\'t support your platform, {platform.system()}.')


def main():
    dir_name = 'lolcats'

    print_header()
    dir_path = get_dir(dir_name)
    get_lolcat(dir_path)
    open_lolcat(dir_path)


if __name__ == '__main__':
    main()
