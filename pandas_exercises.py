from pydataset import data
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
from env import host, user, password
import datetime as dt

#url = f'mysql+pymysql://{user}:{password}@{host}/employees'

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


def dataframe_splain(dataframe, use_name='sample', sample_limit=10):
    print(f'{header_fancy}{use_name.upper()} DATA{Style.RESET_ALL}')
    if sample_limit and len(dataframe) > sample_limit:
        print(dataframe.sample(10))
    else:
        print(dataframe)
    print()
    print(f'{header_fancy}{use_name} details{str(dataframe.shape)}{Style.RESET_ALL}')
    print(dataframe.dtypes)


#print_title('Title_goes_here')
#print_rule('This\nis\nrule\ntext')

clear_screen()

###############################################################################
###############################################################################
###############################################################################

print_title('Exercises')
print_rule(
'''Create a notebook or python script named pandas_exercises to do your work in 
for this exercise.

For the following exercises, you'll need to load several datasets using the 
pydataset library. (If you get an error when trying to run the import below, 
use pip to install the pydataset package.)''', intro_fancy, False, False)
print_rule(
    '''from pydataset import data''', code_fancy)
print_rule(
'''When the instructions say to load a dataset, you can pass the name of the 
dataset as a string to the data function to load the dataset. You can also 
view the documentation for the data set by passing the show_doc keyword 
argument.''', intro_fancy, False, False)
print_rule(
'''mpg = data('mpg') # load the dataset and store it in a variable
# data('mpg', show_doc=True) # view the documentation for the dataset'''
, code_fancy)


###############################################################################
###############################################################################
###############################################################################

print_title(
'''mpg dataset''', title_fancy, True, False)
print_rule(
    '''Load the mpg dataset. Read the documentation for it, and use the data to answer 
these questions:''', intro_fancy, False, False)

mpg = data('mpg')

print(intro_fancy)
data('mpg', show_doc=True)

print('\n' + intro_fancy + str(mpg.sample(10)) + Style.RESET_ALL)

###############################################################################

print_rule('''On average, which manufacturer has the best miles per gallon?''')

mpg['avg_mileage'] = (mpg.cty + mpg.hwy) / 2
mpg_mfg = mpg.groupby('manufacturer').avg_mileage.agg(['count', 'mean', 'min', 'max']).sort_values(by='mean', ascending=False)

###############################################################################

print('\n' + header_fancy + 'mileage by manufacturer' + Style.RESET_ALL)
dataframe_splain(mpg_mfg, "mpg_mfg")

print_rule('''How many different manufacturers are there?''')

###############################################################################

print(f'{Fore.CYAN}There are {Style.BRIGHT}{len(mpg_mfg)}{Style.NORMAL} different manufacturers{Style.RESET_ALL}')

###############################################################################

print_rule('''How many different models are there?''')

mpg_models = mpg.groupby(['manufacturer', 'model']).hwy.agg('count')

print('\n' + header_fancy + 'manufacturers and models' + Style.RESET_ALL)

print(mpg_models)

print(f'\n{Fore.CYAN}There are {Style.BRIGHT}{len(mpg_models)}{Style.NORMAL} different models{Style.RESET_ALL}')

###############################################################################

print_rule('''Do automatic or manual cars have better miles per gallon?''')

go_to_paren = lambda x:  x[0:x.index('(')]
mpg['trans_cat'] = mpg['trans'].apply(go_to_paren)

mpg_trans = mpg.groupby('trans_cat').avg_mileage.agg(['count','mean','min','max'])

print(mpg_trans)

###############################################################################
###############################################################################
###############################################################################

print_title('''Joining and Merging''', title_fancy, True, False)
print_rule('''Copy the users and roles dataframes from the examples above.''', intro_fancy, False )

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})

dataframe_splain(users,'users')
print()
dataframe_splain(roles,'roles')

###############################################################################

print_rule('''What do you think a right join would look like? An outer join?''' )

join_right = pd.merge(users, roles, left_on='role_id', right_on='id', how='right')
join_outer = pd.merge(users, roles, left_on='role_id', right_on='id', how='outer')

print(header_fancy + 'right join' + Style.RESET_ALL)
print(join_right)
print('\n' + header_fancy + 'outer join' + Style.RESET_ALL)
print(join_outer)

###############################################################################

print_rule('''What happens if you drop the foreign keys from the dataframes and try to merge 
them?''')

join_chaos = pd.merge(users, roles)
print(header_fancy + 'chaos join' + Style.RESET_ALL)
print(join_chaos)

###############################################################################
###############################################################################
###############################################################################

print_title('''Getting data from SQL databases''', title_fancy, True, False)
print_rule('''Create a function named get_db_url. It should accept a username, hostname, 
password, and database name and return a url formatted like in the examples in 
this lesson.''', intro_fancy, False)


def get_db_url(user, password, host, database):
    return f'mysql+pymysql://{user}:{password}@{host}/{database}'


print(f'{Style.BRIGHT}{Fore.CYAN}def {Fore.YELLOW}get_db_url{Fore.WHITE}(\
{Fore.CYAN}user{Fore.WHITE}, {Fore.CYAN}host{Fore.WHITE}, \
{Fore.CYAN}password{Fore.WHITE}, {Fore.CYAN}table{Fore.WHITE}):')
print(f'    {Fore.MAGENTA}return {Fore.CYAN}f{Fore.RED}\'mysql+pymysql://\
{Fore.CYAN}\173{Fore.WHITE}user{Fore.CYAN}\175{Fore.RED}:{Fore.CYAN}\173\
{Fore.WHITE}password{Fore.CYAN}\175{Fore.RED}@{Fore.CYAN}\173{Fore.WHITE}host\
{Fore.CYAN}\175{Fore.RED}/{Fore.CYAN}\173{Fore.WHITE}database{Fore.CYAN}\175\
{Fore.RED}\'{Style.RESET_ALL}')

###############################################################################

print_rule('''Use your function to obtain a connection to the employees database.''')

emps_url = get_db_url(user, password, host, 'employees')
#print(emps_url)

employees = pd.read_sql('SELECT * FROM employees', emps_url)


dataframe_splain(employees,'employees')
# print(header_fancy + 'employees table' + Style.RESET_ALL)
# print(employees.sample(10))
# print()
# print(header_fancy + 'employees details - ' + str(employees.shape) + Style.RESET_ALL)
# print(employees.dtypes)

###############################################################################

print_rule('''Once you have successfully run a query:''', intro_fancy, True, False)

print_rule('''Intentionally make a typo in the database url. What kind of error message 
do you see?''')

print(fancify('One shit-ton of error messages', header_fancy))

###############################################################################

print_rule('''Intentionally make an error in your SQL query. What does the error message 
look like?''')

#emps2 = pd.read_sql('SELECT * FROM employee', emps_url)
print(fancify('Another shit-ton of error messages', header_fancy))

###############################################################################

print_rule('''Read the employees and titles tables into two separate dataframes''')

titles = pd.read_sql('SELECT emp_no, title, from_date, (case when to_date > now() then date(now())+1 else to_date end) to_date FROM titles', emps_url)

dataframe_splain(titles, 'titles')
# print(header_fancy + 'titles table' + Style.RESET_ALL)
# print(titles.sample(10))
# print()
# print(header_fancy + 'titles details - ' + str(titles.shape) + Style.RESET_ALL)
# print(titles.dtypes)

###############################################################################

print_rule('''Visualize the number of employees with each title.''')

#title_counts = pd.read_sql('SELECT title, COUNT(*) employees FROM titles WHERE to_date > NOW() GROUP BY title ORDER BY employees DESC', emps_url)
date_today = pd.Timestamp(np.datetime64('today'))
max_to_date = titles.to_date.max()
print('Today\'s Date:', date_today, type(date_today))
max_to_date = pd.Timestamp(max_to_date)
print('Max To Date:', max_to_date, type(max_to_date))

#print('Max Date - Today:', max_to_date - date_today, type((max_to_date - date_today)))

titles.from_date = pd.to_datetime(titles.from_date)  
titles.to_date = pd.to_datetime(titles.to_date)  
titles['is_current'] = titles.to_date > date_today
titles['tenure'] = titles.to_date - titles.from_date
titles['tenure'] = titles.tenure.apply(lambda x: x.days)

dataframe_splain(titles, 'titles')

#print(header_fancy + 'employees by title' + Style.RESET_ALL)
#print(title_counts)

###############################################################################

print_rule('''Join the employees and titles dataframes together.''')

employees_titles = pd.merge(
    employees, 
    titles.rename(columns={'emp_no':'emp_no_t'}), 
    left_on='emp_no', right_on='emp_no_t', how='inner')
dataframe_splain(employees_titles, 'employees_titles')


###############################################################################

print_rule('''Visualize how frequently employees change titles.''')



###############################################################################

print_rule('''For each title, find the hire date of the employee that was hired most recently 
with that title.''')



###############################################################################

print_rule('''Write the code necessary to create a cross tabulation of the number of titles 
by department. (Hint: this will involve a combination of SQL and python/pandas 
code)''')



###############################################################################
###############################################################################
###############################################################################

print_title('''get_db_url''', title_fancy, True, False)

###############################################################################

print_rule(
'''Use your get_db_url function to help you explore the data from the chipotle 
database. Use the data to answer the following questions:''', intro_fancy, False)



###############################################################################

print_rule('''What is the total price for each order?''')



###############################################################################

print_rule('''What are the most popular 3 items?''')


###############################################################################

print_rule('''Which item has produced the most revenue?''')


