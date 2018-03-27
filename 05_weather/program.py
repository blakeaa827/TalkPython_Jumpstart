import requests


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
    r = requests.get(f'http://api.wunderground.com/api/f85a415c3e7425eb/conditions/q/{zip_code}.json')
    if 'error' not in r.json()['response']:
        location = r.json()['current_observation']['display_location']['full']
        temp = r.json()['current_observation']['temp_f']
        weather = r.json()['current_observation']['weather']
        return [location, temp, weather.lower()]
    else:
        return None


def print_weather(result):
    print('The weather in {} is {} F and {}'.format(*result))


if __name__ == '__main__':
    main()
