import requests
from bs4 import BeautifulSoup
from collections import namedtuple


def main():
    print_header()
    while True:
        zip_code = get_zip()
        report = get_weather(zip_code)
        if report:
            print_weather(report)
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
    report = namedtuple('WeatherReport', 'loc, temp, scale, condition')

    for line in soup.findAll('h2'):
        if "Oops! There's been a glitch." in line:
            return None
        else:
            pass

    report.loc = soup.find(id='inner-content').find('h1').get_text().strip()
    report.temp = soup.find(class_='wu-value wu-value-to').get_text().strip()
    report.scale = soup.find(class_='wu-label').get_text().strip()
    report.condition = soup.find(class_='condition-icon small-6 medium-12 columns').p.get_text().lower().strip()
    return report


def print_weather(report):
    print(f'The weather in {report.loc} is {report.temp} {report.scale} and {report.condition}')


if __name__ == '__main__':
    main()
