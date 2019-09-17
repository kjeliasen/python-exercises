#!/bin/env/python -e

import json
import sys




def main():
    # do all the things
    while True:
        for command, (fn, desc) in commands.items():
            print(f'{command:4d}) {desc}')
        command = input('enter the thing to do: ')
        fn = commands.get(command, unknown)
        fn()


def load():
    with open ('checkbook_users.json') as u:
        users(json.load(u))


if __name__ == '__main__':
    main()


commands = {
    '1': (view_balance, 'view balance'),
    '2': record_debit,
    # ...
}


commands['1'] # -> <func view_balance>
commands['2'] # -> <func record_debit>


def view_balance():
    pass


def record_debit():
    pass


def unknown():
    print('wtf, chuck?')
