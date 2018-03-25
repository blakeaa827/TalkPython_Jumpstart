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


def list_journal(journal, new_entries):
    pass


def save_exit(filename, new_lines):
    print(f'... saving new journal entries to {filename} ...')
    with open(filename, 'a') as file:
            file.writelines(new_lines)
    print('... save complete ...')


def add_entry(new_entries):
    pass


def main():
    journal_file = './data/test_journal.jrn'
    journal = load_journal(journal_file)


main()
