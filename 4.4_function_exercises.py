#Exercises

"""
Create a file named 4.4_function_exercises.py for this exercise. After 
creating each function specified below, write the necessary code in order to 
test your function.
"""

"""
1.  Define a function named is_two. It should accept one input and return True 
    if the passed input is either the number or the string 2, False otherwise.
"""

def is_two(num):
    return str(num) == 2

"""
2.  Define a function named is_vowel. It should return True if the passed 
    string is a vowel, False otherwise.
"""
vowels = ['a','e','i','o','u']

def is_vowel(char):
    test = char[0].lower()
    if test == 'y':
        print('Maybe')

    return test in vowels

"""
3.  Define a function named is_consonant. It should return True if the passed 
    string is a consonant, False otherwise. Use your is_vowel function to 
    accomplish this.
"""

def is_consonant(char)
    test = char[0].lower()
    if test.isalpha():
        if test =='y':
            print('Maybe')
        return test not in vowels
    else:
        return False

"""
4.  Define a function that accepts a string that is a word. The function 
    should capitalize the first letter of the word if the word starts with a 
    consonant.
"""

def return_word(chars):
    if is_consonant(chars):
        return chars.capitalize
    else:
        return chars
    

"""
5.  Define a function named calculate_tip. It should accept a tip percentage 
    (a number between 0 and 1) and the bill total, and return the amount to 
    tip.
"""

def calculate_tip(check_amount, tip_percent=.2, tax_amount=0, round_to_dollar=0):
    """
    Calculates tip based on check amount and target tip percentage. Allows choice
    of tip percentage (defaults to .2 - 20%), removal of tax from the tip
    calculation, and the ability to round the final payment up to a set dollar
    multiple (e.g. nearest whole dollar, nearest $5, nearest $10) (or down if 
    less than 10% of the initially-calculated tip)
    """


def calculate_tip(check_amount, tip_percent=.2, tax_amount=0, round_to_dollar=0):
    """
    Calculates tip based on check amount and target tip percentage. Allows choice
    of tip percentage (defaults to .2 - 20%), removal of tax from the tip
    calculation, and the ability to round the final payment up to a set dollar
    multiple (e.g. nearest whole dollar, nearest $5, nearest $10) (or down if 
    less than 10% of the initially-calculated tip)
    """
    tippable_amount = round(check_amount - tax_amount, 2)
    base_tip_amount = round(tippable_amount * tip_percent, 2)
    base_pay_amount = check_amount + base_tip_amount
    if round_to_dollar == 0:
        plus_round = 0
    else:
        above_round = base_pay_amount % round_to_dollar
        if above_round <= base_tip_amount * .10:
            plus_round = -(above_round)
        else:
            plus_round = round_to_dollar - above_round
    tip_amount = base_tip_amount + plus_round
    pay_amount = check_amount + tip_amount
    output_format = 'Check: {Check:>9.2f}\nTip: {Tip:>11.2f} (Base Tip: {BT:>6.2f})\nTotal: {Total:>9.2f}'
    print(output_format.format(Check=check_amount, BT=base_tip_amount, Tip=tip_amount, Total=pay_amount))
    if plus_round:
        print('final tip is {:.1f}%'.format(100*tip_amount/tippable_amount))
    return tip_amount, check_amount


to_tip, to_pay = calculate_tip(53.42,.25,6.75,5)

"""
6.  Define a function named apply_discount. It should accept a original price, 
    and a discount percentage, and return the price after the discount is 
    applied.
"""



"""
7.  Define a function named handle_commas. It should accept a string that is a 
    number that contains commas in it as input, and return a number as output.
"""



"""
8.  Define a function named get_letter_grade. It should accept a number and 
    return the letter grade associated with that number (A-F).
"""



"""
9.  Define a function named remove_vowels that accepts a string and returns a 
    string with all the vowels removed.
"""



"""
10. Define a function named normalize_name. It should accept a string and 
    return a valid python identifier, that is:
        * anything that is not a valid python identifier should be removed
        * leading and trailing whitespace should be removed
        * everything should be lowercase
        * spaces should be replaced with underscores
    
    for example:
        Name will become name
        First Name will become first_name
        % Completed will become completed
"""



"""
11. Write a function named cumsum that accepts a list of numbers and returns a 
    list that is the cumulative sum of the numbers in the list.
        cumsum([1, 1, 1]) returns [1, 2, 3]
        cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]
"""



"""
Bonii
"""



"""
1.  Create a function named twelveto24. It should accept a string in the 
    format 10:45am or 4:30pm and return a string that is the representation of 
    the time in a 24-hour format. Bonus write a function that does the opposite.
"""




"""
2.  Create a function named col_index. It should accept a spreadsheet column 
    name, and return the index number of the column.
        col_index('A') returns 1
        col_index('B') returns 2
        col_index('AA') returns 27
"""

