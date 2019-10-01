from pydataset import data
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
from env import host, user, password
import seaborn as sns
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


def get_db_url(user, password, host, database):
    return f'mysql+pymysql://{user}:{password}@{host}/{database}'


#print_title('Title_goes_here')
#print_rule('This\nis\nrule\ntext')

clear_screen()

###############################################################################
###############################################################################
###############################################################################

print_title('Exercises')

print_rule('''Create a file named 4.9_seaborn_exercises.py for this exercise.''')


###############################################################################
###############################################################################
###############################################################################

print_title('Iris database')

print_rule('''Use the iris database to answer the following quesitons:''')

iris = data('iris')
print(intro_fancy)
data('iris', show_doc=True)
print(Style.RESET_ALL)

frame_splain(iris, 'iris')

print_rule('''What does the distribution of petal lengths look like?''')

sns.distplot(iris['Petal.Length'])
plt.show()

print_rule('''Is there a correlation between petal length and petal width?''')

sns.jointplot(data=iris, x='Petal.Length', y='Petal.Width', kind='reg') 
plt.show()

print_rule('''Would it be reasonable to predict species based on sepal width and sepal 
length?''')

sns.relplot(data=iris, x='Sepal.Length', y='Sepal.Width', hue='Species')      
plt.show()


print_rule('''Which features would be best used to predict species?''')

sns.pairplot(data=iris, hue='Species', kind='reg')  
plt.show()

print_rule('Best predictors are Petal Width and Petal Height', header_fancy)


###############################################################################
###############################################################################
###############################################################################

print_title('Problem 1')


print_rule('''Using the lesson as an example, use seaborn's load_dataset function to load 
the anscombe data set. Use pandas to group the data by the dataset column, 
and calculate summary statistics for each dataset. What do you notice?''')

ans = sns.load_dataset('anscombe')
frame_splain(ans, 'anscombe')

print_rule('''Plot the x and y values from the anscombe data. Each dataset should be in a 
separate column.''')

sns.relplot(data=ans, x='x', y='y', col='dataset', hue='dataset')
plt.show()

###############################################################################
###############################################################################
###############################################################################

print_title('Problem 2')

print_rule('''Load the InsectSprays dataset and read it's documentation. Create a boxplot 
that shows the effectiveness of the different insect sprays.''')

InsectSprays = data('InsectSprays')
print(intro_fancy)
data('InsectSprays', show_doc=True)
print(Style.RESET_ALL)
frame_splain(InsectSprays, 'InsectSprays')

sns.boxplot(data=InsectSprays, y='count', x='spray', hue='spray')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

###############################################################################
###############################################################################
###############################################################################

print_title('Problem 3')

print_rule('''Load the swiss dataset and read it's documentation. Create visualizations to 
answer the following questions:''')

swiss = data('swiss')
print(intro_fancy)
data('swiss', show_doc=True)
print(Style.RESET_ALL)
frame_splain(swiss, 'swiss')

sns.distplot(swiss.Catholic, bins=10)
plt.show()

print_rule('''Create an attribute named is_catholic that holds a boolean value of whether or 
not the province is Catholic. 

(Choose a cutoff point for what constitutes catholic)''')

swiss['is_catholic'] = swiss.Catholic > 75
frame_splain(swiss, "swiss", 0)

print_rule('''Does whether or not a province is Catholic influence fertility?''')

sns.boxplot(data=swiss, y='Fertility', x='is_catholic', hue='is_catholic')
plt.show()

print_rule('Yes, Catholicism correlates with fertility', header_fancy)

print_rule('''What measure correlates most strongly with fertility?''')

sns.heatmap(swiss.corr(), annot=True, cmap='Reds')

#sns.pairplot(data=swiss, vars=['Fertility','Agriculture','Examination','Education','Catholic','Infant.Mortality'], kind='reg')
sns.heatmap(swiss.corr(), annot=True, cmap='Reds')
plt.show()
print_rule('Education correlates most strongly with fertility', header_fancy)

###############################################################################
###############################################################################
###############################################################################

print_title('Problem 4')

print_rule('''Using the chipotle dataset from the previous exercise, create a bar chart that 
shows the 4 most popular items and the revenue produced by each.''')

chp_url = get_db_url(user, password, host, 'chipotle')
#print(emps_url)

orders = pd.read_sql('SELECT * FROM orders', chp_url)
frame_splain(orders, 'orders')
orders['price_val'] = orders.item_price.apply(lambda x: float(x.replace('$','').replace(',','')))
item_revenues = orders.groupby('item_name').price_val.agg(['count', 'sum']).sort_values(['count','sum'], ascending = False)
item_revenues['item'] = item_revenues.index
item_revenues = item_revenues.rename(columns={'count':'orders', 'sum':'revenues'})
frame_splain(item_revenues, 'item_revenues')

top_items = item_revenues[:4]
frame_splain(top_items, 'top_items')

pal = sns.color_palette("Blues_d", len(top_items))
g=sns.barplot(x='item', y='orders', data=top_items)
for index, row in top_items.iterrows():
    g.annotate = (round(row.revenues,2))
plt.show()



###############################################################################
###############################################################################
###############################################################################

print_title('Problem 5')

print_rule('''Load the sleepstudy data and read it's documentation. Use seaborn to create a 
line chart of all the individual subject's reaction times and a more prominant 
line showing the average change in reaction time.''')


