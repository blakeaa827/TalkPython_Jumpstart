import requests
from bs4 import BeautifulSoup


def main():
    print_header()
    while True:
        zip_code = get_zip()
        result = get_weather(zip_code)
        if result:
            print_weather(result)
        else:
            print("I'm unable to locate that zip code.  Try again.")
            continue


def print_header():
    print('---------------------------------------')
    print('           WEATHER APP')
    print('---------------------------------------')
    print()


def get_zip():
    while True:
        zip_code = input('Please enter a zip code or E[x]it: ')
        if zip_code == 'x':
            exit(0)
        elif len(zip_code) != 5:
            print('That does not appear to be a valid zip code.')
            continue
        else:
            try:
                int(zip_code)
                return str(zip_code)
            except ValueError:
                print('That does not appear to be a valid zip code.')
                continue


def get_weather(zip_code):
    r = requests.get(f'http://www.wunderground.com/weather/{zip_code}')
    soup = BeautifulSoup(r.text, 'html.parser')

    for line in soup.findAll('h2'):
        if "Oops! There's been a glitch." in line:
            return None
        else:
            pass

    location = soup.find(id='inner-content').find('h1').get_text().strip()
    temp = soup.find(class_='wu-value wu-value-to').get_text().strip()
    weather = soup.find(class_='condition-icon small-6 medium-12 columns').p.get_text().lower().strip()
    print(weather)
    return [location, temp, weather]


def print_weather(result):
    print('The weather in {} is {} F and {}'.format(*result))


if __name__ == '__main__':
    main()
