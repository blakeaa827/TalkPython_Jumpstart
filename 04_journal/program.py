import os.path


def print_banner():
    print('----------------------------------------')
    print('         PERSONAL JOURNAL APP')
    print('----------------------------------------')
    print()


def load_journal(filename):
    if not os.path.isfile(filename) and not os.path.islink(filename):
        print(f'... journal file \'{filename}\' does not exist ...')
        print('... initializing new journal ...')
        with open(filename, 'x') as file:
            pass
        return []
    else:
        print(f'... loading journal entries from {filename} ...')
        journal = []
        with open(filename, 'r') as file:
            for line in file:
                journal += [line]
        print(f'... loaded {len(journal)} items')
        return journal


def add_entry(new_entries):
    return new_entries.append([input('Enter new journal entry below\n')])


def list_journal(journal, new_entries):
    line_number = 1
    if journal:
        for line in journal:
            print(f'{line_number}. {line}')
            line_number += 1
    elif new_entries:
        for line in new_entries:
            print(f'{line_number}. {line}')
            line_number += 1
    else:
        print('No entries to display')


def save_exit(filename, new_lines):
    print(f'... saving new journal entries to {filename} ...')
    with open(filename, 'a') as file:
            file.writelines(new_lines)
    print('... save complete ...')


def get_command():
    command = input('What would you like to do? [L]ist, [A]dd, E[x]it: ').lower()
    if command == 'l':
        return 'list'
    elif command == 'a':
        return 'add'
    elif command == 'x':
        return 'exit'
    else:
        return None


def main():
    journal_file = './data/test_journal.jrn'
    journal = load_journal(journal_file)
    new_lines = []

    while True:
        command = get_command()
        if command == 'list':
            list_journal(journal, new_lines)
        elif command == 'add':
            new_lines = add_entry(new_lines)
        elif command == 'exit':
            save_exit(journal_file, new_lines)
            exit(0)
        else:
            print('That is not a valid command. Try again.')


main()
