from pydataset import data
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

from colorama import init, Fore, Back, Style

txt=''
title_fancy = Style.BRIGHT + Fore.YELLOW + Back.BLUE
rule_fancy = Style.NORMAL + Fore.YELLOW + Back.BLUE
intro_fancy = Style.NORMAL + Fore.YELLOW + Back.BLACK
demo_fancy = Style.NORMAL + Fore.CYAN + Back.BLACK
header_fancy = Style.BRIGHT + Fore.CYAN + Back.BLACK
code_fancy = Style.NORMAL + Fore.BLACK + Back.WHITE

def fancify(text, fancy=Style.BRIGHT):
    return f'{fancy}{str(text)}{Style.RESET_ALL}'


def print_title(text, fancy=title_fancy, upline=True, downline=True):
    if upline:
        print ()
    print(star_line(fancy))
    print(star_title(text, fancy))
    print(star_line(fancy))
    if downline:
        print()

def print_rule(text, fancy=rule_fancy, upline=True, downline=True):
    text_lines = text.split('\n')
    if upline:
        print()
    for line in text_lines:
        print(fancify(f'{line:<80s}', fancy))
    if downline:
        print()


def star_line(fancy=Style.BRIGHT):
    return(f'{fancy}{txt:*^80s}{Style.RESET_ALL}')


def star_title(text, fancy=Style.BRIGHT):
    title_text = f'  {text}  ' 
    star_text = f'{title_text:*^80s}' if len(text) < 70 else text
    return(f'{fancy}{star_text}{Style.RESET_ALL}')


def clear_screen():
    print('\033[2J')


#print_title('Title_goes_here')
#print_rule('This\nis\nrule\ntext')

clear_screen()

print_title('Exercises')
print_rule(
'''Create a notebook or python script named pandas_exercises to do your work in 
for this exercise.

For the following exercises, you'll need to load several datasets using the 
pydataset library. (If you get an error when trying to run the import below, 
use pip to install the pydataset package.)''', intro_fancy, False, False)


print_rule('''from pydataset import data''', code_fancy)

print_rule(
'''When the instructions say to load a dataset, you can pass the name of the 
dataset as a string to the data function to load the dataset. You can also 
view the documentation for the data set by passing the show_doc keyword 
argument.''', intro_fancy, False, False)

print_rule('''mpg = data('mpg') # load the dataset and store it in a variable
# data('mpg', show_doc=True) # view the documentation for the dataset''', code_fancy)

print_title('''mpg dataset''', title_fancy, True, False)

print_rule(
    '''Load the mpg dataset. Read the documentation for it, and use the data to answer 
these questions:''', intro_fancy, False, False)

print_rule('''On average, which manufacturer has the best miles per gallon?''')

print_rule('''How many different manufacturers are there?''')

print_rule('''How many different models are there?''')

print_rule('''Do automatic or manual cars have better miles per gallon?''')

print_title('''Joining and Merging''', title_fancy, True, False)


print_rule('''Copy the users and roles dataframes from the examples above.''', intro_fancy, False )

print_rule('''What do you think a right join would look like? An outer join?''' )

print_rule('''What happens if you drop the foreign keys from the dataframes and try to merge 
them?''')

print_title('''Getting data from SQL databases''', title_fancy, True, False)


print_rule('''Create a function named get_db_url. It should accept a username, hostname, 
password, and database name and return a url formatted like in the examples in 
this lesson.''', intro_fancy, False)

print_rule('''Use your function to obtain a connection to the employees database.''')

print_rule('''Once you have successfully run a query:''')

print_rule('''Intentionally make a typo in the database url. What kind of error message 
do you see?''')

print_rule('''Intentionally make an error in your SQL query. What does the error message 
look like?''')

print_rule('''Read the employees and titles tables into two separate dataframes''')

print_rule('''Visualize the number of employees with each title.''')

print_rule('''Join the employees and titles dataframes together.''')

print_rule('''Visualize how frequently employees change titles.''')

print_rule('''For each title, find the hire date of the employee that was hired most recently 
with that title.''')

print_rule('''Write the code necessary to create a cross tabulation of the number of titles 
by department. (Hint: this will involve a combination of SQL and python/pandas 
code)''')

print_title('''get_db_url''', title_fancy, True, False)

print_rule(
'''Use your get_db_url function to help you explore the data from the chipotle 
database. Use the data to answer the following questions:''', intro_fancy, False)

print_rule('''What is the total price for each order?''')

print_rule('''What are the most popular 3 items?''')

print_rule('''Which item has produced the most revenue?''')
