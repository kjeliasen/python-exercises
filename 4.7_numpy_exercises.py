# Exercises
# Create a file named 4.7_numpy_exercises.py for this exercise.

import numpy as np
import math

def print_header(header):
    txt = ''
    header = '  ' + header + '  '
    print(f'\n\n{txt:*^80s}')
    print(f'{header:*^80s}')
    print(f'{txt:*^80s}\n\n')


print_header('Original Exercises')

# Use the following code for the questions below:

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
print(f'Original array a: \n{a}\n')


# Make Functions

def get_negatives(array):
    return array[array < 0]


def get_positives(array):
    return array[array > 0]


def get_odds(array):
    return array[array % 2 == 1]


def get_evens(array):
    return array[array % 2 == 0]


def get_even_positives(array):
    return get_positives(get_evens(array))


def get_squares(array):
    return array ** 2


def centered(array):
    return array - array.mean()


def get_z_score(array):
    return centered(array) / array.std()


# How many negative numbers are there?

print(f'The {len(get_negatives(a))} negatives in a: \n{get_negatives(a)}\n')


# How many positive numbers are there?

print(f'The {len(get_positives(a))} positives in a: \n{get_positives(a)}\n')


# How many even positive numbers are there?

print(f'Even positives: \n{len(get_even_positives(a))}\n')


# If you were to add 3 to each data point, how many positive numbers would there be?

print(f'Positives after adding 3: \n{len(get_positives(a + 3))}\n')


# If you squared each number, what would the new mean and standard deviation be?

print(f'Squared a: \n{get_squares(a)}\n')
print(f'Mean of squared a: {get_squares(a).mean()}')
print(f'Standard deviation of squared a: {get_squares(a).std()}')


# A common statistical operation on a dataset is centering. This means to 
# adjust the data such that the center of the data is at 0. This is done by 
# subtracting the mean from each data point. Center the data set.

print(f'Centered a: \n{centered(a)}\n')


# Calculate the z-score for each data point. Recall that the z-score is given by:
#     Z = x − μ / σ

print(f'Z-scores for a: \n{get_z_score(a)}\n')



# Copy the setup and exercise directions from More Numpy Practice into your 
# 4.7_numpy_exercises.py and add your solutions.
#     (file location: 
#     https://gist.github.com/ryanorsinger/c4cf5a64ec33c014ff2e56951bc8a42d)


# Life w/o numpy to life with numpy

## Setup 1
print_header('Setup 1')

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = np.array(a)

print(f'New array a: \n{a}\n')

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the 
# numbers in above list

sum_of_a = a.sum()

print(f'Sum of a: {sum_of_a}')


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the 
# numbers in the above list

min_of_a = a.min()

print(f'Min of a: {min_of_a}')


# Exercise 3 - Make a variable named max_of_a to hold the max number of all 
# the numbers in the above list

max_of_a = a.max()

print(f'Max of a: {max_of_a}')


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the 
# numbers in the above list

mean_of_a = a.mean()

print(f'Mean of a: {mean_of_a}')


# Exercise 5 - Make a variable named product_of_a to hold the product of 
# multiplying all the numbers in the above list together

product_of_a = np.product(a)

print(f'Product of a: {product_of_a}')


# Exercise 6 - Make a variable named squares_of_a. It should hold each number 
# in a squared like [1, 4, 9, 16, 25...]

squares_of_a = get_squares(a)

print(f'Squares of a: \n{squares_of_a}\n')


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd 
# numbers

odds_in_a = get_odds(a)

print(f'Odds in a: \n{odds_in_a}\n')


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = get_evens(a)

print(f'Evens in a: \n{get_evens(a)}\n')


# What about life in two dimensions? A list of lists is matrix, a table, a 
# spreadsheet, a chessboard...

# Setup 2: 
print_header('Setup 2')

# Consider what it would take to find the sum, min, max, average, sum, product, 
# and list of squares for this list of two lists.

b = [
    [3, 4, 5],
    [6, 7, 8]
]
b = np.array(b)

print(f'Array b: \n{b}\n')

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. 
# **Hint, you'll first need to make sure that the "b" variable is a numpy array**

# sum_of_b = 0
# for row in b:
#     sum_of_b += sum(row)

sum_of_b = b.sum()

print(f'Sum of b: {sum_of_b}')


# Exercise 2 - refactor the following to use numpy. 

# min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

min_of_b = b.min()

print(f'Min of b: {min_of_b}')


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.

# max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

max_of_b = b.max()

print(f'Max of b: {max_of_b}')



# Exercise 4 - refactor the following using numpy to find the mean of b

# mean_of_b = (sum(b[0]) + sum(b[1])) / (len([b[0]]) + len(b[1]))

mean_of_b = b.mean()

print(f'Mean of b: {mean_of_b}')


# Exercise 5 - refactor the following to use numpy for calculating the product 
# of all numbers multiplied together.

# product_of_b = 1
# for row in b:
#     for number in row:
#         product_of_b *= number

product_of_b = np.product(b)

print(f'Product of b: {product_of_b}')


# Exercise 6 - refactor the following to use numpy to find the list of squares 

# squares_of_b = []
# for row in b:
#     for number in row:
#         squares_of_b.append(number**2)

squares_of_b = get_squares(b)

print(f'Squares of b: \n{squares_of_b}\n')


# Exercise 7 - refactor using numpy to determine the odds_in_b

# odds_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 != 0):
#             odds_in_b.append(number)

odds_in_b = get_odds(b)

print(f'Odds in b: \n{odds_in_b}\n')


# Exercise 8 - refactor the following to use numpy to filter only the even numbers

# evens_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 == 0):
#             evens_in_b.append(number)

evens_in_b = get_evens(b)

print(f'Odds in b: \n{evens_in_b}\n')


# Exercise 9 - print out the shape of the array b.

print(f'Shape of b: \n{np.shape(b)}\n')


# Exercise 10 - transpose the array b.

print(f'Transposed b: \n{b.T}')


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

b_reshape = b.reshape(1, 6)

print(f'Reshaped b: \n{b_reshape}\n')

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

b_listed = b.reshape(6,1).tolist()

print(f'Listed elements of b: \n{b_listed}\n')

## Setup 3
print_header('Setup 3')

c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
c = np.array(c)

print(f'Array c: \n{c}\n')

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.

sum_of_c = c.sum()
min_of_c = c.min()
max_of_c = c.max()
product_of_c = np.product(c)

print(f'Sum of c: {sum_of_c}')
print(f'Min of c: {min_of_c}')
print(f'Max of c: {max_of_c}')
print(f'Product of c: {product_of_c}')


# Exercise 2 - Determine the standard deviation of c.

std_of_c = c.std()

print(f'Standard deviation of c: {std_of_c}')


# Exercise 3 - Determine the variance of c.

var_of_c = c.var()

print(f'Varaince of c: {var_of_c}')


# Exercise 4 - Print out the shape of the array c

print(f'Shape of c: \n{np.shape(c)}\n')


# Exercise 5 - Transpose c and print out transposed result.

c_transposed = c.T

print(f'Transposed c: \n{c_transposed}\n')



# Exercise 6 - Multiply c by the c-Transposed and print the result.

c_times_c_t = c * c.T

print(f'Multiplied c by c-Transposed: \n{c_times_c_t}\n')


# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

print(f'Sum of c times c-Transposed: {c_times_c_t.sum()}')
assert c_times_c_t.sum() == 261

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

print(f'Product of c times c-Transposed: {np.product(c_times_c_t)}')
assert np.product(c_times_c_t) == 131681894400



# Setup 4
print_header('Setup 4')

d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
d = np.array(d)

print(f'Array d: \n{d}\n')

# Exercise 1 - Find the sine of all the numbers in d

rads = np.pi / 180
d_rads = d * rads
d_sine = np.sin(d_rads)

print(f'Radians of d: \n{d_rads}\n')

print(f'Sines of d: \n{d_sine.round(8)}\n')

# Exercise 2 - Find the cosine of all the numbers in d

d_cosine = np.cos(d_rads)

print(f'Cosines of d: \n{d_cosine.round(8)}\n')


# Exercise 3 - Find the tangent of all the numbers in d

d_tangent = np.tan(d_rads)

print(f'Tangents of d: \n{d_tangent.round(8)}\n')


# Exercise 4 - Find all the negative numbers in d

print(f'Negatives in d: \n{get_negatives(d)}\n')


# Exercise 5 - Find all the positive numbers in d

print(f'Positives in d: \n{get_positives(d)}\n')


# Exercise 6 - Return an array of only the unique numbers in d.



# Exercise 7 - Determine how many unique numbers there are in d.



# Exercise 8 - Print out the shape of d.

print(f'Shape of d: \n{np.shape(d)}\n')


# Exercise 9 - Transpose and then print out the shape of d.

print(f'Transposed d: \n{d.T}')


# Exercise 10 - Reshape d into an array of 9 x 2


