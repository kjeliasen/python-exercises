

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

"""
    How many different ways can you combine the letters from "abc" with the 
    numbers 1, 2, and 3?
"""


"""
    How many different ways can you combine two of the letters from "abcd"?
"""


"""
    Save this file as profiles.json inside of your exercises directory. Use 
    the load function from the json module to open this file, it will produce 
    a list of dictionaries. 

https://gist.githubusercontent.com/ryanorsinger/f77e5ec94dbe14e21771/raw/d4a1f916723ca69ac99fdcab48746c6682bf4530/profiles.json

    Using this data, write some code that calculates and outputs the following 
    information:

"""

"""
    Total number of users
"""

"""
    Number of active users
"""

"""
    Number of inactive users
"""

"""
    Grand total of balances for all users
"""

"""
    Average balance per user
"""

"""
    User with the lowest balance
"""

"""
    User with the highest balance
"""

""" 
    Most common favorite fruit
"""

"""
    Least most common favorite fruit
"""

"""
    Total number of unread messages for all users
"""
