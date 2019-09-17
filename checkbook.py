#!/bin/env/python -e

import json
import sys
import calendar as c
import datetime as dt
import time as t


is_running = False


def main():
    try:
    # do all the things
        while True:
            print(is_running)
            for command, (fn, desc) in commands.items():
                print(f'{command:>20s}) {desc}')
            command = input('enter the thing to do: ')
            fn_tuple = commands.get(command, unknown)
            fn = fn_tuple[0]
            # print(fn)
            fn()
    except Exception as e:
        print(e)


def load(users, accounts, transactions, file='checkbook_accounts.json'):
    with open(file) as fin:
        data(json.load(fin))
    users = data['users']
    accounts = data['accounts']
    transactions = data['transactions']
    return users, accounts, transactions

def save(users, accounts, transactions, file='checkbook_accounts.json'):
    data = dict(
        users = users,
        accounts = accounts,
        transactions = transactions
    )
    with open(file) as fout:
        json.dump(data, fout)


def view_balance():
    print('view balance')
    pass


def record_debit():
    print('record debit')
    pass


def record_credit():
    print('record credit')
    pass


def change_user():
    print('change user')
    pass


def change_account():
    print('change amount')
    pass


def bailout():
    print('Bailout')
    raise Exception('user selected exit')


def unknown():
    print('wtf, chuck?')



commands = {
    '1': (view_balance, 'View Balance'),
    '2': (record_debit, 'Make Deposit'),
    '3': (record_credit, 'Withdraw Funds'),
    '4': (change_user, 'Change User'),
    '5': (change_account, 'Change Account'),
    'X': (bailout, 'Exit')
    # ...
}


if __name__ == '__main__':
    is_running = True
    main()

