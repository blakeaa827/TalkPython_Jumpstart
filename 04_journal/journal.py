import os


def build_path(name):
    return os.path.join('.', 'data', name + '.jrn')


def load(name):
    """
    Load the requested journal
    :param name: filename of the requested journal excluding the file extension
    :return: journal data structure as a list
    """
    jrn_path = build_path(name)
    if not os.path.exists(jrn_path):
        print(f'... journal file \'{jrn_path}\' does not exist ...')
        print('... initializing new journal ...')
        with open(jrn_path, 'w') as file:
            pass
        return []
    else:
        print(f'... loading journal entries from {jrn_path} ...')
        journal = []
        with open(jrn_path, 'r') as file:
            for line in file:
                journal.append(line.rstrip())
        print(f'... loaded {len(journal)} items')
        return journal


def save_exit(name, data):
    """
    save journal and exit program
    :param name: filename of the working journal excluding the file extension
    :param data: list containing journal entries
    :return: None
    """
    jrn_path = build_path(name)
    print(f'... saving new journal entries to {jrn_path} ...')
    with open(jrn_path, 'w') as file:
        for line in data:
            file.write(line + '\n')
    print('... save complete ...')
