"""
Exercises
Create a file named 4.7_numpy_exercises.py for this exercise.
"""
import numpy as np


"""
Use the following code for the questions below:
"""
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

"""
How many negative numbers are there?
"""
def get_negatives(array):
    return array[array < 0]

print(f'Negatives: {len(get_negatives(a))}')

"""
How many positive numbers are there?
"""
def get_positives(array):
    return array[array > 0]

print(f'Positives: {len(get_positives(a))}')

"""
How many even positive numbers are there?
"""
def get_odds(array):
    return array[array % 2 == 1]

def get_evens(array):
    return array[array % 2 == 0]

def get_even_positives(array):
    return get_positives(get_evens(array))

print(f'Even positives: {len(get_even_positives(a))}')

"""
If you were to add 3 to each data point, how many positive numbers would there be?
"""

print(f'Positives after adding 3: {len(get_positives(a + 3))}')

"""
If you squared each number, what would the new mean and standard deviation be?
"""

print(f'a-squared: {(a ** 2)}')
print(f'Mean of a-squared: {(a ** 2).mean()}')
print(f'Standard deviation of a-squared: {(a ** 2).std()}')

"""
A common statistical operation on a dataset is centering. This means to adjust 
the data such that the center of the data is at 0. This is done by subtracting 
the mean from each data point. Center the data set.
"""


def centered(array):
    return array - array.mean()


print(f'Centered a: {centered(a)}')

"""
Calculate the z-score for each data point. Recall that the z-score is given by:

Z = x − μ / σ
"""


def get_z_score(array):
    return centered(array) / array.std()


print(f'Z-scores for a: {get_z_score(a)}')


"""
Copy the setup and exercise directions from More Numpy Practice into your 4.7_numpy_exercises.py and add your solutions.
"""