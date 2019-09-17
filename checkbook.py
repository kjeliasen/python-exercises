#!/bin/env/python -e

import json
import sys
import calendar as c
import datetime as dt
import time as t




def main():
    # do all the things
    while True:
        for command, (fn, desc) in commands.items():
            print(f'{command:4d}) {desc}')
        command = input('enter the thing to do: ')
        fn = commands.get(command, unknown)
        fn()


def load(users, accounts, transactions):
    with open('checkbook_accounts.json') as fin:
        data(json.load(fin))
    users = data['users']
    accounts = data['accounts']
    transactions = data['transactions']
    return users, accounts, transactions

def save(users, accounts, transactions):
    data = dict(
        users = users,
        accounts = accounts,
        transactions = transactions
    )
    with open('checkbook_accounts.json') as fout:
        json.dump(data, fout)


if __name__ == '__main__':
    main()


commands = {
    '1': (view_balance, 'View Balance'),
    '2': (record_debit, 'Make Deposit'),
    '3': (record_credit 'Withdraw Funds'),
    '4': (change_user, 'Change User'),
    '5': (change_account, 'Change Account'),
    'X': (bailout, 'Exit')
    # ...
}


commands['1'] # -> <func view_balance>
commands['2'] # -> <func record_debit>


def view_balance():
    print('view balance')
    pass


def record_debit():
    print('record ')
    pass


def unknown():
    print('wtf, chuck?')
