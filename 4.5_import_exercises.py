###Exercises

"""
    Create a file named 4.5_import_exercises.py to do your work in.
"""

"""
    Import and test 3 of the functions from your functions exercise file.

    Your functions exercise are not currently in a file with a name that can 
    be easily imported. Copy your functions exercise file and name the copy 
    functions_exercises.py.

    Import each function in a different way:


"""

"""
    import the module and refer to the function with the . syntax
    
>>> import function_exercises
>>> function_exercises.is_vowel('A')
True
"""

import function_exercises
print(function_exercises.is_vowel('A'))

"""
    use from to import the function directly

>>> from function_exercises import twelveto24
>>> twelveto24('12:01am')
'0:01'
"""

from function_exercises import twelveto24
twelveto24('12:01am')


"""
    use from and give the function a different name

>>> from function_exercises import calculate_tip as ct

"""
from function_exercises import calculate_tip as ct
print(ct(75.43,.2,0,10))
    


# For the following exercises, read about and use the itertools module from 
# the standard library to help you solve the problem.

import itertools as it


"""
    How many different ways can you combine the letters from "abc" with the 
    numbers 1, 2, and 3?
"""
combine_ABC_123 = [p for p in it.product('ABC', '123')]  
print(str(len(combine_ABC_123)) + ' combinations:')
print(combine_ABC_123)


"""
    How many different ways can you combine two of the letters from "abcd"?
"""
permutations_abcd = [p for p in it.permutations('abcd', 2)]
print(str(len(permutations_abcd)) + ' permutations')
print(permutations_abcd)


"""
    Save this file as profiles.json inside of your exercises directory. Use 
    the load function from the json module to open this file, it will produce 
    a list of dictionaries. 

https://gist.githubusercontent.com/ryanorsinger/f77e5ec94dbe14e21771/raw/d4a1f916723ca69ac99fdcab48746c6682bf4530/profiles.json

    Using this data, write some code that calculates and outputs the following 
    information:

"""
import json
with open('profiles.json', 'r') as f:
    profiles = json.load(f)

"""
    Total number of users
"""
users = len(profiles)
print('{} users'.format(users))


"""
    Number of active users
"""
users_active = sum([1 for p in profiles if p['isActive']])
print('{} active users'.format(users_active)) 


"""
    Number of inactive users
"""
users_inactive = sum([1 for p in profiles if not p['isActive']])
print('{} inactive users'.format(users_inactive)) 


"""
    Grand total of balances for all users
"""
bals = [(float(p['balance'].replace('$','').replace(',','')), p['name']) for p in profiles]
total_balance = sum([b[0] for b in bals])
print('{} total balance for all users'.format(total_balance)) 


"""
    Average balance per user
"""
average_balance = total_balance / users
print('The average user balance is {:.2f}'.format(average_balance))


"""
    User with the lowest balance
"""
lowest_balance = min([b[0] for b in bals])
lowest_balance_users = [b[1] for b in bals if b[0] == lowest_balance]
print('The lowest balance is {:.2f}, which is held by:'.format(lowest_balance))
for lbu in lowest_balance_users:
    print(lbu)


"""
    User with the highest balance
"""
highest_balance = max([b[0] for b in bals])
highest_balance_users = [b[1] for b in bals if b[0] == highest_balance]
print('The highest balance is {:.2f}, which is held by:'.format(highest_balance))
for hbu in highest_balance_users:
    print(hbu)


""" 
    Most common favorite fruit

    Least most common favorite fruit
"""
user_favorite_fruits = [p['favoriteFruit'] for p in profiles]
favorite_fruit_set = set(user_favorite_fruits)
favorite_fruits = []
for item in favorite_fruit_set:
    fruit_name = item
    fav_count = sum([1 for pick in user_favorite_fruits if pick == item])
    favorite_fruits.append([fruit_name, fav_count])

max_fav_count = max([f[1] for f in favorite_fruits])
min_fav_count = min([f[1] for f in favorite_fruits])
most_favorite_fruit = [f[0] for f in favorite_fruits if f[1] == max_fav_count]
least_favorite_fruit = [f[0] for f in favorite_fruits if f[1] == min_fav_count]

print('The most common favorite fruit is {}, while the least common is {}.'.format(most_favorite_fruit[0], least_favorite_fruit[0]))


"""
    Total number of unread messages for all users
"""
unread_messages = 0
greetings = [p['greeting'] for p in profiles]
for g in greetings:
    g_chars = []
    for c in g:
        if c in '0123456789':
            g_chars.append(c)
    unread_messages += int(''.join(g_chars))
    # print(g, unread_messages)
print('There are {} unread messages'.format(unread_messages))
    

