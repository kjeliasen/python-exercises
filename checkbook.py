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
    print(f'Exit {__name__}')


def bug_note(func, verb='checking', **kwargs):
    print(f'DEBUG: {verb} fn({func})')
    if len(kwargs.items()):
        print([f'{key} == {value}' for key, value in kwargs.items()])


def load(file=entries_file_load):
    func = 'load'
    bug_note(verb='starting', func=func)
    with open(file) as fin:
        data = json.load(fin)
    got_users = data['users']
    got_accounts = data['accounts']
    got_entries = data['entries']
    bug_note(verb='ending', func=func)
    return got_users, got_accounts, got_entries


def save(users, accounts, entries, file=entries_file_save):
    func = 'save'    
    bug_note(verb='starting', func=func)
    data = {
        'users': users,
        'accounts': accounts,
        'entries': entries
    }
    with open(file, 'w') as fout:
        json.dump(data, fout, indent=2)
    bug_note(verb='ending', func=func)


def get_cur_user_info(cur_user_id, users):
    func = 'get_cur_user_info'    
    bug_note(verb='starting', func=func)
    for user in users:
        if user['user_id'] == cur_user_id:
            bug_note(verb='ending', func=func)
            return user
    bug_note(verb='ending', func=func)
    return {
        'user_id': '0',
        'first_name': 'NO USER',
        'last_name': 'SELECTED'
    }


def get_cur_account_info(accounts):
    func = 'get_cur_account_info'    
    bug_note(verb='starting', func=func)
    for account in accounts:
        if account['account_id'] == cur_account_id:
            bug_note(verb='ending', func=func)
            return account
    bug_note(verb='ending', func=func)
    return {
        'acct_id': '0',
        'acct_ref_name': 'NO ACCOUNT SELECTED'
    }


def get_cur_user_accounts(accounts):
    func = 'get_cur_user_accounts'    
    bug_note(verb='looping', func=func)
    return [account for account in accounts if account['account_id'] == cur_account_id]
      

def get_cur_account_entries(entries):
    func = 'get_cur_account_entries'    
    bug_note(verb='looping', func=func)
    return [entry for entry in entries if entry['account_id'] == cur_account_id]
    

def cl_view_balance(context, **kwargs):
    func = 'cl_view_balance'    
    bug_note(verb='starting', func=func)
    # do some of the things
    print('Viewing Balance')
    bug_note(verb='ending', func=func)
    # return context
    

def cl_record_debit(context, **kwargs):
    func = 'cl_record_debit'    
    bug_note(verb='starting', func=func)
    # do some of the things
    print('Recording Debit')
    bug_note(verb='ending', func=func)
    # return context
    

def cl_record_credit(context, **kwargs):
    func = 'cl_record_credit'    
    bug_note(verb='starting', func=func)
    # do some of the things
    print('Recording Credit')
    bug_note(verb='ending', func=func)
    # return context
    

def cl_change_user(context, **kwargs):
    func = 'cl_change_user'    
    bug_note(verb='starting', func=func)
    print('Changing User')
    # do some of the things
    # print([f'{key} == {value}' for key, value in kwargs.items()])
    # print(kwargs['users'])
    context['current_user_id'] = kwargs['users'][0]
    bug_note(verb='ending', func=func)
    # return context
    

def cl_change_account(context, **kwargs):
    func = 'cl_change_account'    
    bug_note(verb='starting', func=func)
    # do some of the things
    print('change amount')
    bug_note(verb='ending', func=func)
    # return context
    

def cl_get_users_info(context, **kwargs):
    func = 'cl_get_users_info'    
    bug_note(verb='starting', func=func)
    # do some of the things
    print(users)
    bug_note(verb='ending', func=func)
    # return context
    

def cl_get_accounts_info(context, **kwargs):
    func = 'cl_get_accounts_info'    
    bug_note(verb='starting', func=func)
    # do some of the things
    print(accounts)
    bug_note(verb='ending', func=func)
    # return context
    

def cl_get_entries_info(context, **kwargs):
    func = 'cl_get_entries_info'    
    bug_note(verb='starting', func=func)
    # do some of the things
    print(entries)
    bug_note(verb='ending', func=func)
    # return context
    

def cl_dictionary_info(context, **kwargs):
    func = 'cl_dictionary_info'    
    bug_note(verb='starting', func=func)
    # do some of the things
    print(users, accounts, entries)
    bug_note(verb='ending', func=func)
    # return context
    

def cl_save_file(context, **kwargs):
    func = 'cl_save_file'    
    bug_note(verb='starting', func=func)
    # do some of the things
    save(users, accounts, entries, entries_file_save)
    bug_note(verb='ending', func=func)
    # return context
    

def cl_gtfo(context, **kwargs):
    func = 'cl_gtfo'    
    bug_note(verb='starting', func=func)
    print('User selected \'exit\'')
    raise UserExitException


def unknown(context, **kwargs):
    func = 'unknown'    
    bug_note(verb='encountering', func=func)
    print('wtf, chuck?')


def update_user_variables(user_id):
    func = 'update_user_variables'    
    bug_note(verb='starting', func=func)
    user_info = {}
    for account in accounts:
        if account['user_id'] == cur_user_id:
            bug_note(verb='ending', func=func)
            user_info = account
            break
    bug_note(verb='ending', func=func)
    return user_info


def init_command_list():
    func = 'init_command_list'    
    bug_note(verb='starting', func=func)
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
        'X': (cl_gtfo, 'Exit')
        # ...
    }
    bug_note(verb='ending', func=func)
    return setcommands

def init_context():
    func = 'init_context'    
    bug_note(verb='starting', func=func)
    setcontext = {
        'current_user_id': False,
        'current_account_id': False,
        'data_dirty': False
    } 
    bug_note(verb='ending', func=func)
    return setcontext              


def main():
    func = 'main'    
    bug_note(verb='starting', func=func)
    commands = init_command_list()
    context = init_context()
    users, accounts, entries = load(entries_file_load)
    # cur_user_accounts = get_cur_user_accounts
    # cur_account_entries = get_cur_account_entries
    # new_account_entries = []
    do_command = False
    # cur_user_accounts = 

    try:
    # do all the things
        while True:
            print('\n\n')
            if not context['current_user_id']:
                print('DEBUG no current user')
                do_command = '4'
            else:
                print('DEBUG found current user')
                cur_user_info = get_cur_user_info(users)
                print('Current user is {} {}'.format(cur_user_info['first_name'], cur_user_info['last_name']))
                #print(cur_user_info)
                pass
            if not do_command:
                for command, (fn, desc) in commands.items():
                    print(f'{command:>20s}) {desc}')
                print('\n')
                do_command = input('Enter the thing to do: ')
                print('\n\n')
            fn = commands.get(do_command, (unknown, "Unknown"))
            print(f'DEBUG: Selected fn == {fn[1]}')
            fn = fn[0]
            fn(context=context, users=users, accounts=accounts, entries=entries)
            do_command = False
            bug_note(verb='reiterating', func=func)
            
    except Exception as e:
        print('EXCEPTION RAISED')
        print(e)
        print(context)

    bug_note(verb='ending', func=func)
        

if __name__ == '__main__':
    # print(os.getcwd())
    main()

