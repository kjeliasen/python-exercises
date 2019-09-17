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
cur_user_dict = {}
cur_account_dict = {}
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


def load(file=transactions_file_load):
    with open(file) as fin:
        data = json.load(fin)
    got_users = data['users']
    got_accounts = data['accounts']
    got_transactions = data['transactions']
    return got_users, got_accounts, got_transactions


def save(file=transactions_file_save):
    data = {
        'users': users,
        'accounts': accounts,
        'transactions': transactions
    }
    with open(file, 'w') as fout:
        json.dump(data, fout, indent=2)


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


def get_users_info():
    print(users)
    pass


def get_accounts_info():
    print(accounts)
    pass


def get_transactions_info():
    print(transactions)
    pass


def dictionary_info():
    print(users, accounts, transactions)
    pass


def save_file():
    save(transactions_file_save)
    pass


def bailout():
    print('User selected \'exit\'')
    raise UserExitException


def unknown():
    print('wtf, chuck?')


def update_user_variables(user_id):
    user_info = {}
    for account in accounts:
        if account['user_id'] == cur_user_id:
            user_info = account
            break
    return user_info

def init_command_list():
    setcommands = {
        '1': (view_balance, 'View Balance'),
        '2': (record_debit, 'Make Deposit'),
        '3': (record_credit, 'Withdraw Funds'),
        '4': (change_user, 'Change User'),
        '5': (change_account, 'Change Account'),
        'C': (get_users_info, 'Check Users Data'),
        'A': (get_accounts_info, 'Check Accounts Data'),
        'T': (get_transactions_info, 'Check Transactions Data'),
        'D': (dictionary_info, 'Check Dictionary Data'),
        'S': (save_file, 'Save File'),
        'X': (bailout, 'Exit')
        # ...
    }
    return setcommands


if __name__ == '__main__':
    commands = init_command_list()
    users, accounts, transactions = load(transactions_file_load)
    # print(os.getcwd())
    main()

