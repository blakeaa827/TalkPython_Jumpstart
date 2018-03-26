import os.path
import journal


def main():
    jrn_file = 'test'
    jrn = journal.load(jrn_file)

    while True:
        cmd = get_cmd()
        if cmd == 'list':
            print_jrn(jrn)
        elif cmd == 'add':
            jrn.append(new_entry())
        elif cmd == 'exit':
            journal.save_exit(jrn_file, jrn)
            exit(0)
        else:
            print('That is not a valid command. Try again.')


def print_banner():
    print('----------------------------------------')
    print('         PERSONAL JOURNAL APP')
    print('----------------------------------------')
    print()


def get_cmd():
    cmd = input('What would you like to do? [L]ist, [A]dd, E[x]it: ').lower().strip()
    if cmd == 'l':
        return 'list'
    elif cmd == 'a':
        return 'add'
    elif cmd == 'x':
        return 'exit'
    else:
        return None


def print_jrn(data):
    if not data:
        print('No entries to display')
        return()
    else:
        for i, line in enumerate(reversed(data)):
            print(f'{i + 1}. {line}')
        return()


def new_entry():
    return input('Enter new journal entry below\n')


if __name__ == '__main__':
    main()
