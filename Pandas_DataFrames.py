from pydataset import data
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

from colorama import init, Fore, Back, Style

txt=''
title_fancy = Style.BRIGHT + Fore.BLUE + Back.WHITE
rule_fancy = Style.NORMAL + Fore.BLUE + Back.WHITE
intro_fancy = Style.NORMAL + Fore.YELLOW + Back.BLACK

def fancify(text, fancy=Style.BRIGHT):
    return f'{fancy}{str(text)}{Style.RESET_ALL}'


def print_title(text, fancy=title_fancy):
    print(star_line(fancy))
    print(star_title(text, fancy))
    print(star_line(fancy), '\n')

def print_rule(text, fancy=rule_fancy):
    text_lines = text.split('\n')
    print ('\n')
    for line in text_lines:
        print(fancify(f'{line:<80s}', fancy))
    print ('\n')


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
'''For several of the following exercises, you'll need to load several datasets 
using the pydataset library. (If you get an error when trying to run the 
import below, use pip to install the pydataset package.)

When the instructions say to load a dataset, you can pass the name of the 
dataset as a string to the `data` function to load the dataset. You can also 
view the documentation for the data set by passing the show_doc keyword 
argument.

    # data('mpg', show_doc=True) # view the documentation for the dataset
    # mpg = data('mpg') # load the dataset and store it in a variable

# All the datasets loaded from the pydataset library will be pandas dataframes.''',
intro_fancy)


print_title('Problem 1')
print_rule('Copy the code from the lesson to create a dataframe full of student grades.', intro_fancy)


print_rule('''1.a Create a column named passing_english that indicates whether each student 
has a passing grade in reading.''')


print_rule('''1.b Sort the english grades by the passing_english column. How are duplicates 
handled?''')


print_rule('''1.c Sort the english grades first by passing_english and then by student name. 
All the students that are failing english should be first, and within the 
students that are failing english they should be ordered alphabetically. The 
same should be true for the students passing english. (Hint: you can pass a 
list to the .sort_values method)''')


print_rule('''1.d Sort the english grades first by passing_english, and then by the actual 
english grade, similar to how we did in the last step.''')


print_rule('''1.e Calculate each students overall grade and add it as a column on the 
dataframe. The overall grade is the average of the math, english, and reading 
grades.''')



print_title('''Problem 2''')

print_rule('''Load the mpg dataset. Read the documentation for the dataset and use it for the 
following questions:''', intro_fancy)

print_rule('''2.a How many rows and columns are there?''')



print_rule('''2.b What are the data types of each column?''')


print_rule('''2.c Summarize the dataframe with .info and .describe''')


print_rule('''2.d Rename the cty column to city.''')


print_rule('''2.e Rename the hwy column to highway.''')


print_rule('''2.f Do any cars have better city mileage than highway mileage?''')


print_rule('''2.g Create a column named mileage_difference this column should contain the 
difference between highway and city mileage for each car.''')


print_rule('''2.h Which car (or cars) has the highest mileage difference?''')


print_rule('''2.i Which compact class car has the lowest highway mileage? The best?''')



print_rule('''2.j Create a column named average_mileage that is the mean of the city and 
highway mileage.''')



print_rule('''2.k Which dodge car has the best average mileage? The worst?''')



print_title('Problem 3')


print_rule('''Load the Mammals dataset. Read the documentation for it, and use the data to 
answer these questions:''', intro_fancy)


print_rule('''3.a How many rows and columns are there?''')


print_rule('''3.2 What are the data types?''')


print_rule('''3.3 Summarize the dataframe with .info and .describe''')


print_rule('''3.4 What is the the weight of the fastest animal?''')


print_rule('''3.5 What is the overal percentage of specials?''')


print_rule('''3.6 How many animals are hoppers that are above the median speed? 
What percentage is this?''')
