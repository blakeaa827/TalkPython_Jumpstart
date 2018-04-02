import os
import collections


def main():
    banner()
    search_folder, search_text = get_params()
    search_files(search_folder, search_text, list())


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


def search_files(folder, text, results):
    Result = collections.namedtuple('search_result',
                                    'file, line_number, line_text')
    for file in os.listdir(folder):
        abs_file_path = os.path.join(os.path.abspath(folder), file)
        if os.path.isdir(abs_file_path):
            search_files(abs_file_path, text, results)
        else:
            try:
                with open(abs_file_path, 'r', encoding='utf-8') as fin:
                    for line_number, line in enumerate(fin):
                        if text in line:
                            results.append(Result(
                                file=abs_file_path,
                                line_number=line_number,
                                line_text=line.rstrip()
                            ))
                            print(f'result {len(results)}: ', end='')
                            print_result(results[-1])
            except UnicodeDecodeError:
                pass
    return results


def print_result(result):
    print(
        result.file,
        f'\n  line {result.line_number}: "{result.line_text}"'
    )


if __name__ == '__main__':
    main()
