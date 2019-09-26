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
intro_fancy, False,)

print_title('Problem 1', title_fancy, True, False)
print_rule('Copy the code from the lesson to create a dataframe full of student grades.', intro_fancy, False)

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

print(df)


print_rule('''1.a Create a column named passing_english that indicates whether each student 
has a passing grade in reading.''')

df['passing_english'] = df['english'] > 69

print(df)

print_rule('''1.b Sort the english grades by the passing_english column. How are duplicates 
handled?''')

print(df.sort_values(by='passing_english'))


print_rule('''1.c Sort the english grades first by passing_english and then by student name. 
All the students that are failing english should be first, and within the 
students that are failing english they should be ordered alphabetically. The 
same should be true for the students passing english. (Hint: you can pass a 
list to the .sort_values method)''')

print(df.sort_values(by=['passing_english', 'name']))


print_rule('''1.d Sort the english grades first by passing_english, and then by the actual 
english grade, similar to how we did in the last step.''')

print(df.sort_values(by=['passing_english', 'english']))


print_rule('''1.e Calculate each students overall grade and add it as a column on the 
dataframe. The overall grade is the average of the math, english, and reading 
grades.''')

df['overall_grade'] = (df['english'] + df['math'] + df['reading']) / 3

print(df)

print_title('''Problem 2''', title_fancy, True, False)

print_rule('''Load the mpg dataset. Read the documentation for the dataset and use it for the 
following questions:''', intro_fancy, False, False)

mpg = data('mpg')
print('\n' + intro_fancy + str(mpg.sample(10)) + Style.RESET_ALL)


print_rule('''2.a How many rows and columns are there?''')

print(f'mpg dimensions: {fancify(mpg.shape)}')
print(f'\n{fancify(len(mpg))} records in dataset')

print_rule('''2.b What are the data types of each column?''')

print(mpg.dtypes, '\n')

print_rule('''2.c Summarize the dataframe with .info and .describe''')

print(f'{header_fancy}mpg.info{Style.RESET_ALL}')
print(mpg.info())
print(f'\n{header_fancy}mpg.describe{Style.RESET_ALL}')
print(mpg.describe())

print_rule('''2.d Rename the cty column to city.''')

mpg = mpg.rename(columns={'cty': 'city'})
print(mpg.sample(10))

print_rule('''2.e Rename the hwy column to highway.''')

mpg = mpg.rename(columns={'hwy': 'highway'})
print(mpg.sample(5))

print_rule('''2.f Do any cars have better city mileage than highway mileage?''')

print(mpg[mpg['city'] > mpg['highway']])

print_rule('''2.g Create a column named mileage_difference this column should contain the 
difference between highway and city mileage for each car.''')

mpg['mileage_difference'] = mpg['highway'] - mpg['city']
print(mpg.sample(10))

print_rule('''2.h Which car (or cars) has the highest mileage difference?''')

print(mpg[mpg['mileage_difference'] == mpg['mileage_difference'].max() ])

print_rule('''2.i Which compact class car has the lowest highway mileage? The best?''')

mpg_compact = mpg[mpg['class'] == 'compact']
#print(mpg_compact.highway.max())
print(mpg_compact[(mpg_compact.highway == mpg_compact.highway.max()) | (mpg_compact.highway == mpg_compact.highway.min())])


print_rule('''2.j Create a column named average_mileage that is the mean of the city and 
highway mileage.''')

mpg['average_mileage'] = (mpg.city + mpg.highway) / 2
print(mpg.sample(10))

print_rule('''2.k Which dodge car has the best average mileage? The worst?''')

dodge_max_mileage = mpg[mpg.manufacturer == 'dodge'].average_mileage.max()
dodge_min_mileage = mpg[mpg.manufacturer == 'dodge'].average_mileage.min()

print(mpg[((mpg.manufacturer == 'dodge') & ((mpg.average_mileage == dodge_max_mileage) | (mpg.average_mileage == dodge_min_mileage)))].sort_values(by='average_mileage', ascending=False))

print_title('Problem 3', title_fancy, True, False)


print_rule('''Load the Mammals dataset. Read the documentation for it, and use the data to 
answer these questions:''', intro_fancy, False, False)

mams = data('Mammals')
print('\n' + intro_fancy + str(mams.sample(10)) + Style.RESET_ALL)

print_rule('''3.a How many rows and columns are there?''')


print(f'mams dimensions: {fancify(mams.shape)}')

print_rule('''3.2 What are the data types?''')

print(mams.dtypes)

print_rule('''3.3 Summarize the dataframe with .info and .describe''')

print(f'{header_fancy}mams.info{Style.RESET_ALL}')
print(mams.info())
print(f'\n{header_fancy}mams.describe{Style.RESET_ALL}')
print(mams.describe())


print_rule('''3.4 What is the the weight of the fastest animal?''')

print(mams[mams.speed == mams.speed.max()].weight)

print_rule('''3.5 What is the overal percentage of specials?''')

print(f'{(100*(len(mams[mams.specials])/len(mams))):.2f}&')

print_rule('''3.6 How many animals are hoppers that are above the median speed? 
What percentage is this?''')

mams_speed_median = mams.speed.median()
hoppers_faster_than_median = len(mams[((mams.hoppers) & (mams.speed > mams_speed_median))])
print(f'{demo_fancy}Median speed: {header_fancy}{mams_speed_median}{Style.RESET_ALL}')
print(f'{demo_fancy}Hoppers faster than {mams_speed_median}: {header_fancy}{hoppers_faster_than_median}, or {(hoppers_faster_than_median / len(mams)):.2f}%{Style.RESET_ALL}')

