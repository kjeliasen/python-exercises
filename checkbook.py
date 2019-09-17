#!/bin/env/python -e

import json
import sys
import calendar as c
import datetime as dt
import time as t
import os



# Declare Global Variables
transactions_file_load = 'checkbook_accounts.json'
transactions_file_save = 'checkbook_accounts_saves.json'
cur_user = '0'
cur_account = '000'
cur_user_dict = {}
cur_account_dict = {}
cur_transactions = {}
data = {}


class UserExitException(Exception):
    print('User Selected Exit')


def main():
    commands = init_command_list()
    users, accounts, transactions = load(transactions_file_load)

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
            fn(cur_user, cur_account, users, accounts, transactions)
    except Exception as e:
        print(e)


def load(file=transactions_file_load):
    with open(file) as fin:
        data = json.load(fin)
    got_users = data['users']
    got_accounts = data['accounts']
    got_transactions = data['transactions']
    return got_users, got_accounts, got_transactions


def save(users, accounts, transactions, file=transactions_file_save):
    data = {
        'users': users,
        'accounts': accounts,
        'transactions': transactions
    }
    with open(file, 'w') as fout:
        json.dump(data, fout, indent=2)


def cl_view_balance(cur_user, cur_account, users, accounts, transactions):
    print('view balance')
    pass


def cl_record_debit(cur_user, cur_account, users, accounts, transactions):
    print('record debit')
    pass


def cl_record_credit(cur_user, cur_account, users, accounts, transactions):
    print('record credit')
    pass


def cl_change_user(cur_user, cur_account, users, accounts, transactions):
    print('change user')
    pass


def cl_change_account(cur_user, cur_account, users, accounts, transactions):
    print('change amount')
    pass


def cl_get_users_info(cur_user, cur_account, users, accounts, transactions):
    print(users)
    pass


def cl_get_accounts_info(cur_user, cur_account, users, accounts, transactions):
    print(accounts)
    pass


def cl_get_transactions_info(cur_user, cur_account, users, accounts, transactions):
    print(transactions)
    pass


def cl_dictionary_info(cur_user, cur_account, users, accounts, transactions):
    print(users, accounts, transactions)
    pass


def cl_save_file(cur_user, cur_account, users, accounts, transactions):
    save(users, accounts, transactions, transactions_file_save)
    pass


def cl_bailout(cur_user, cur_account, users, accounts, transactions):
    print('User selected \'exit\'')
    raise UserExitException


def unknown(cur_user, cur_account, users, accounts, transactions):
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
        '1': (cl_view_balance, 'View Balance'),
        '2': (cl_record_debit, 'Make Deposit'),
        '3': (cl_record_credit, 'Withdraw Funds'),
        '4': (cl_change_user, 'Change User'),
        '5': (cl_change_account, 'Change Account'),
        'C': (cl_get_users_info, 'Check Users Data'),
        'A': (cl_get_accounts_info, 'Check Accounts Data'),
        'T': (cl_get_transactions_info, 'Check Transactions Data'),
        'D': (cl_dictionary_info, 'Check Dictionary Data'),
        'S': (cl_save_file, 'Save File'),
        'X': (cl_bailout, 'Exit')
        # ...
    }
    return setcommands


if __name__ == '__main__':
    # print(os.getcwd())
    main()

