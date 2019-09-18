#!/bin/env/python -e

import json
import sys
import calendar as c
import datetime as dt
import time as t
import os



# Declare Global Variables
entries_file_load = 'checkbook_accounts.json'
entries_file_save = 'checkbook_accounts_saves.json'
cur_user_id = '0'
cur_account_id = '0'
new_entries = []


class UserExitException(Exception):
    print('User Selected Exit')




def load(file=entries_file_load):
    with open(file) as fin:
        data = json.load(fin)
    got_users = data['users']
    got_accounts = data['accounts']
    got_entries = data['entries']
    return got_users, got_accounts, got_entries


def save(users, accounts, entries, file=entries_file_save):
    data = {
        'users': users,
        'accounts': accounts,
        'entries': entries
    }
    with open(file, 'w') as fout:
        json.dump(data, fout, indent=2)


def get_cur_user_info(cur_user_id, users):
    for user in users:
        if user['user_id'] == cur_user_id:
            return user
    return {
        'user_id': '0',
        'first_name': '',
        'last_name': 'NO USER SELECTED'
    }


def get_cur_account_info(accounts):
    for account in accounts:
        if account['account_id'] == cur_account_id:
            return account
    return {
        'acct_id': '0',
        'acct_ref_name': 'NO ACCOUNT SELECTED'
    }


def get_cur_user_accounts(accounts):
    return [account for account in accounts if account['account_id'] == cur_account_id]
      

def get_cur_account_entries(entries):
    return [entry for entry in entries if entry['account_id'] == cur_account_id]
    

def cl_view_balance(context, users, accounts, entries):
    # do some of the things
    print('view balance')
    

def cl_record_debit(context, users, accounts, entries):
    # do some of the things
    print('record debit')
    

def cl_record_credit(context, users, accounts, entries):
    # do some of the things
    print('record credit')
    

def cl_change_user(context, users, accounts, entries):
    # do some of the things
    print('change user')
    

def cl_change_account(context, users, accounts, entries):
    # do some of the things
    print('change amount')
    

def cl_get_users_info(context, users, accounts, entries):
    # do some of the things
    print(users)
    

def cl_get_accounts_info(context, users, accounts, entries):
    # do some of the things
    print(accounts)
    

def cl_get_entries_info(context, users, accounts, entries):
    # do some of the things
    print(entries)
    

def cl_dictionary_info(context, users, accounts, entries):
    # do some of the things
    print(users, accounts, entries)
    

def cl_save_file(context, users, accounts, entries):
    # do some of the things
    save(users, accounts, entries, entries_file_save)
    

def cl_bailout(context, users, accounts, entries):
    print('User selected \'exit\'')
    raise UserExitException


def unknown(cusers, accounts, entries):
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
        'T': (cl_get_entries_info, 'Check entries Data'),
        'D': (cl_dictionary_info, 'Check Dictionary Data'),
        'S': (cl_save_file, 'Save File'),
        'X': (cl_bailout, 'Exit')
        # ...
    }
    return setcommands

def init_context():
    setcontext = {
        'current_user_id': 0
        'current_account_id': 0
        'data_dirty': False
    }


def main():
    commands = init_command_list()
    context = init_context()
    users, accounts, entries = load(entries_file_load)
    cur_user_info = get_cur_user_info
    cur_user_accounts = get_cur_user_accounts
    cur_account_entries = get_cur_account_entries
    new_account_entries = []
    # cur_user_accounts = 

    try:
    # do all the things
        while True:
            print('\n\n')
            print(f'Current user is {cur_user_info['first_name']} {cur_user_info['last_name']}')
            for command, (fn, desc) in commands.items():
                print(f'{command:>20s}) {desc}')
            print('\n')
            command = input('Enter the thing to do: ')
            print('\n\n')
            fn = commands.get(command, (unknown, "Unknown"))
            fn = fn[0]
            fn(context, users, accounts, entries)
            
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # print(os.getcwd())
    main()

