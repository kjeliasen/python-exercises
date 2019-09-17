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
    save(transactions, users, accounts)


def load(username):
    with open(f'checkbook_{username}.json') as fin:
        data = json.load(fin))
    transactions = data['transactions']
    accounts = data['accounts']
    users = data['users']
    return transactions, users, accounts

def save(username, transactions, users, accounts):
    data = dict(
        users=user
        transactions=transactions,
        accounts=accounts,
    )
    with open(f'checkbook_{username}.json', 'w') as fout:
        json.dump(fout, data)



if __name__ == '__main__':
    main()


commands = {
    '1': (view_balance, 'view balance'),
    '2': record_debit,
    # ...
}


def view_balance():
    pass


def record_debit():
    pass


def unknown():
    print('wtf, chuck?')
