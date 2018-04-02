import os
import collections


def main():
    banner()
    search_folder, search_text = get_params()
    result_count = 0
    for result in search_dir(search_folder, search_text):
        result_count += 1
        print(result_count)


def banner():
    print('---------------------------------')
    print('        FILE SEARCHER APP')
    print('---------------------------------')
    print()


def get_params():
    while True:
        search_folder = os.path.abspath(input(
            'What folder would you like to search?\n> '
        ))
        if not os.path.isdir(search_folder):
            print(
                'That does not appear to be a valid directory. ',
                'Pleas try again.'
            )
        else:
            break
    search_text = input('For what text should I search?\n> ')
    return search_folder, search_text


def search_dir(folder, text):
    for file in os.listdir(folder):
        abs_file_path = os.path.join(os.path.abspath(folder), file)
        if os.path.isdir(abs_file_path):
            yield from search_dir(abs_file_path, text)
        else:
            yield from search_file(abs_file_path, text)


def search_file(file, text):
    Result = collections.namedtuple('search_result',
                                    'file, line_number, line_text')
    try:
        with open(file, 'r', encoding='utf-8') as fin:
            for line_number, line in enumerate(fin):
                if text in line:
                    yield Result(
                        file=file,
                        line_number=line_number,
                        line_text=line.rstrip()
                    )
    except UnicodeDecodeError:
        pass


def print_result(result):
    print(
        result.file,
        f'\n  line {result.line_number}: "{result.line_text}"'
    )


if __name__ == '__main__':
    main()
