#!/bin/env/python -e

import json
import sys
import calendar as c
import datetime as dt
import time as t
import os



# Declare Global Variables
commands = {}
transactions_file_load = 'checkbook_accounts.json'
transactions_file_save = 'checkbook_accounts_saves.json'
cur_user_id = '0'
cur_account_id = '000'
cur_transaction_id = '0'
cur_transactions = {}
users = {}
accounts = {}
transactions = {}
data = {}


class UserExitException(Exception):
    print('User Selected Exit')


def main():
    try:
    # do all the things
        while True:
            print('\n\n')
            for command, (fn, desc) in commands.items():
                print(f'{command:>20s}) {desc}')
            print('\n')
            command = input('Enter the thing to do: ')
            print('\n\n')
            fn = commands.get(command, (unknown, "Unknown"))
            fn = fn[0]
            fn()
    except Exception as e:
        print(e)


def load(users, accounts, transactions, file=transactions_file_load):
    with open(file) as fin:
        data = json.load(fin)
    users = data['users']
    accounts = data['accounts']
    transactions = data['transactions']
    return users, accounts, transactions


def save(users, accounts, transactions, file=transactions_file_save):
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
    print('User selected \'exit\'')
    raise UserExitException


def unknown():
    print('wtf, chuck?')


def init_command_list():
    setcommands = {
        '1': (view_balance, 'View Balance'),
        '2': (record_debit, 'Make Deposit'),
        '3': (record_credit, 'Withdraw Funds'),
        '4': (change_user, 'Change User'),
        '5': (change_account, 'Change Account'),
        'X': (bailout, 'Exit')
        # ...
    }
    load(users, accounts, transactions, transactions_file_load)
    return setcommands


if __name__ == '__main__':
    commands = init_command_list()
    main()

