#!/usr/bin/env python
# coding: utf-8

# # Exercises
# Make a file named `pandas_series.py` or `pandas_series.ipynb` for the following exercises.

# In[236]:


import pandas as pd
import numpy as np
import math
#get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

from colorama import init, Fore, Back, Style
def fancify(text, fancy=Style.BRIGHT):
    return f'{fancy}{str(text)}{Style.RESET_ALL}'
def print_title(text):
    return print(fancify(fancify(text, Fore.BLUE + Back.CYAN)) + '\n')


# ## 1. Use pandas to create a Series from the following data:
# 
# `["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]`

# In[21]:


task_1a=('1.a. Name the variable that holds the series fruits.')


# In[69]:


print_title(task_1a)

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", 
                    "honeycrisp apple", "tomato", "watermelon", "honeydew", 
                    "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", 
                    "gooseberry", "papaya"])
print(fruits)


# In[23]:


task_1b = '1.b. Run .describe() on the series to see what describe returns for a series of strings.'


# In[24]:


print_title(task_1b)
print(fruits.describe())


# In[26]:


task_1c = '1.c. Run the code necessary to produce only the unique fruit names.'


# In[238]:


print_title(task_1c)

fruit_names = pd.Series(fruits.unique())

print(fruit_names)


# In[57]:


task_1d = '1.d. Determine how many times each value occurs in the series.'


# In[58]:


print_title(task_1d)

fruit_list = fruits.value_counts()

print(fruit_list)


# In[31]:


task_1e = '1.e. Determine the most frequently occurring fruit name from the series.'


# In[187]:


print_title(task_1e)

print(fruit_list.idxmax())


# In[34]:


task_1f = '1.f. Determine the least frequently occurring fruit name from the series.'


# In[203]:


print_title(task_1f)

least_frequent = fruits.value_counts().min()

print(fruit_list[fruit_list == least_frequent])


# In[36]:


task_1g = '1.g .Write the code to get the longest string from the fruits series.'


# In[66]:


print_title(task_1g)

print(fruits[fruits.apply(len).idxmax()])


# In[67]:


task_1h = '1.h. Find the fruit(s) with 5 or more letters in the name.'


# In[68]:


print_title(task_1h)

print(fruits[fruits.apply(len) > 4])


# In[ ]:


task_1i = 'i. Capitalize all the fruit strings in the series.'


# In[71]:


print_title(task_1i)

print(fruits.str.capitalize())


# In[73]:


task_1j = '1.j. Count the letter "a" in all the fruits (use string vectorization)'


# In[107]:


print_title(task_1j)

print(fruits.apply(lambda x: [x, sum([1 for xc in x if xc.lower() == 'a'])]))


# In[76]:


task_1k = '1.k. Output the number of vowels in each and every fruit.'


# In[108]:


print_title(task_1k)

print(fruits.apply(lambda x: [x, sum([1 for xc in x if xc.lower() in 'aeiou'])]))


# In[88]:


task_1l = '1.l. Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.'


# In[90]:


print_title(task_1l)

print(fruits[fruits.apply(lambda x: sum([1 for xc in x if xc.lower() == 'o']) > 1)])


# In[109]:


task_1m = '1.m. Write the code to get only the fruits containing "berry" in the name'


# In[118]:


print_title(task_1m)

print(fruits[fruits.apply(lambda x: 'berry' in x.lower())])


# In[114]:


task_1n = '1.n. Write the code to get only the fruits containing "apple" in the name'


# In[117]:


print_title(task_1n)

print(fruits[fruits.apply(lambda x: 'apple' in x.lower())])


# In[119]:


task_1o = '1.o. Which fruit has the highest amount of vowels'


# In[123]:


print_title(task_1o)

print(fruits[fruits.apply(lambda x: sum([1 for xc in x if xc.lower() in 'aeiou'])).idxmax()])


# ## 2. Use pandas to create a Series from the following data:
# 
# `['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']`

# In[195]:


Series2 = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', 
                     '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', 
                     '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', 
                     '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', 
                     '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])
Series2.name = 'Series2'
print(Series2)


# In[196]:


task_2a = '2.a What is the data type of the series?'


# In[205]:


print_title(task_2a)

print(Series2.dtype)


# In[198]:


task_2b = '2.b. Use series operations to convert the series to a numeric data type.'


# In[219]:


print_title(task_2b)

amounts = Series2.apply(lambda wrd: float(''.join([ltr for ltr in wrd if ltr in '1234567890.'])))

print(amounts)


# In[130]:


task_2c = '2.c. What is the maximum value? The minimum?'


# In[220]:


print_title(task_2c)

print(f'Minimum value = {Fore.GREEN}${amounts.min():>12.2f}{Style.RESET_ALL}')
print(f'Maximum value = {Fore.GREEN}${amounts.max():>12.2f}{Style.RESET_ALL}')


# In[132]:


task_2d = '2.d. Bin the data into 4 equally sized intervals and show how many values fall into each bin.'


# In[223]:


print_title(task_2d)

amount_bins = pd.cut(amounts, 4)

print(amount_bins)
print_title('Counts by bin')
print(amount_bins.value_counts())


# In[134]:


task_2e = '2.e. Plot a histogram of the data. Be sure to include a title and axis labels.'


# In[239]:


print_title(task_2e)

#print(type(amount_bins))
amounts.plot.hist()
plt.show()


# ## 3. Use pandas to create a Series from the following exam scores:
# 
# `[60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]`

# In[146]:


Series3 = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])
Series3.name = 'Series3'
print(Series3)


# In[147]:


task_3a = '3.a What is the minimum exam score? The max, mean, median?'


# In[249]:


print_title(task_3a)

print(Series3.describe())
print(f'\n{Fore.CYAN}{Back.BLACK}Series3 25% pulled by describe() index value:{Style.RESET_ALL}', Series3.describe()['25%'])


# In[149]:


task_3b = '3.b. Plot a histogram of the scores.'


# In[250]:


print_title(task_3b)

Series3.plot.hist()
plt.show()


# In[168]:


task_3c = "3.c. Convert each of the numbers above into a letter grade. \n"    "For example, 86 should be a 'B' and 95 should be an 'A'."


# In[264]:


print_title(task_3c)

bin_grades = lambda pdS: pd.cut(pdS.apply(round), [0,59,69,79,89,100], labels=['F','D','C','B','A'])

grade_bins = bin_grades(Series3)

grades_num_ltr = pd.DataFrame(list(zip(Series3,grade_bins)), columns=['Score', 'Grade'])

print(grades_num_ltr)


# In[174]:


task_3d = '3.d Write the code necessary to implement a curve. I.e. that grade \n'    'closest to 100 should be converted to a 100, and that many points \n'    'should be given to every other score as well.'


# In[271]:


print_title(task_3d)

grade_buffer = 100 - Series3.max()
new_grades = Series3 + grade_buffer
new_grade_bins = bin_grades(new_grades)

grades_change_chart = pd.DataFrame(
    list(zip(Series3,grade_bins,new_grades,new_grade_bins)),
    columns=['Orig Score','Orig Grade','New Score','New Grade'])
print(grades_change_chart)


# ## 4. Use pandas to create a Series from the following string:
# 
# `'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'`

# In[277]:


String4 = 'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
Series4 = pd.Series(list(String4))

print(Series4)


# In[177]:


task_4a = '4.a. What is the most frequently occuring letter? Least frequently occuring?'


# In[284]:


print_title(task_4a)

Letters_list = Series4.value_counts()
print(Letters_list)

highest_frequency = Letters_list.max()
lowest_frequency = Letters_list.min()

letters_used_most = Letters_list[Letters_list == highest_frequency]
letters_used_least = Letters_list[Letters_list == lowest_frequency]

print(fancify(fancify('Most frequent:\n',Fore.GREEN)),letters_used_most)
print(fancify(fancify('Least frequent:\n',Fore.RED)),letters_used_least)


# In[179]:


task_4b = '4.b. How many vowels are in the list?'


# In[290]:


print_title(task_4b)

vowel_count = sum(Letters_list[list('aeiou')])

print(vowel_count)


# In[181]:


task_4c = '4.c. How many consonants are in the list?'


# In[291]:


print_title(task_4c)

print(sum(Letters_list) - vowel_count)


# In[183]:


task_4d = '4.d. Create a series that has all of the same letters, but uppercased'


# In[293]:


print_title(task_4d)

Series4_upper = Series4.str.upper()
print(Series4_upper)


# In[184]:


task_4e = '4.e. Create a bar plot of the frequencies of the 6 most frequently occuring letters.'


# In[333]:


print_title(task_4e)

#top_six_count = Letters_list[5]
#Top_six_letters = Letters_list[Letters_list >= top_six_count]
print(fancify('Top Six Letters'))
Top_six_letters = Letters_list[Letters_list >= Letters_list[5]]
print(Top_six_letters)
#top_six_string = ''.join(list(Top_six_letters.index))
#Top_six_letters.plot.bar()
Letters_list[Letters_list >= Letters_list[5]].plot.bar()
plt.show()

# In[ ]:




