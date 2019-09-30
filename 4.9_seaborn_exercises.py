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


def frame_splain(dataframe, use_name='sample', sample_limit=10):
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

print_rule('''Create a file named 4.9_seaborn_exercises.py for this exercise.''')



print_rule('''Use the iris database to answer the following quesitons:''')



print_rule('''What does the distribution of petal lengths look like?''')



print_rule('''Is there a correlation between petal length and petal width?''')



print_rule('''Would it be reasonable to predict species based on sepal width and sepal 
length?''')



print_rule('''Which features would be best used to predict species?''')



###############################################################################
###############################################################################
###############################################################################

print_title('Problem 1')


print_rule('''Using the lesson as an example, use seaborn's load_dataset function to load 
the anscombe data set. Use pandas to group the data by the dataset column, 
and calculate summary statistics for each dataset. What do you notice?''')



print_rule('''Plot the x and y values from the anscombe data. Each dataset should be in a 
separate column.''')

###############################################################################
###############################################################################
###############################################################################

print_title('Problem 2')

print_rule('''Load the InsectSprays dataset and read it's documentation. Create a boxplot 
that shows the effectiveness of the different insect sprays.''')



###############################################################################
###############################################################################
###############################################################################

print_title('Problem 3')

print_rule('''Load the swiss dataset and read it's documentation. Create visualizations to 
answer the following questions:''')



print_rule('''Create an attribute named is_catholic that holds a boolean value of whether or 
not the province is Catholic. 

(Choose a cutoff point for what constitutes catholic)''')



print_rule('''Does whether or not a province is Catholic influence fertility?''')



print_rule('''What measure correlates most strongly with fertility?''')



###############################################################################
###############################################################################
###############################################################################

print_title('Problem 4')

print_rule('''Using the chipotle dataset from the previous exercise, create a bar chart that 
shows the 4 most popular items and the revenue produced by each.''')



###############################################################################
###############################################################################
###############################################################################

print_title('Problem 5')

print_rule('''Load the sleepstudy data and read it's documentation. Use seaborn to create a 
line chart of all the individual subject's reaction times and a more prominant 
line showing the average change in reaction time.''')


