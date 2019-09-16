#Exercises

"""
Create a file named 4.4_function_exercises.py for this exercise. After 
creating each function specified below, write the necessary code in order to 
test your function.
"""


def is_two(num):
    """
    1.  Define a function named is_two. It should accept one input and return 
    True if the passed input is either the number or the string 2, False 
    otherwise.

    >>> is_two(2)
    True
    >>> is_two('2')
    True
    >>> is_two('tWo')
    True
    >>> is_two(3)
    False
    """
    return str(num).lower() in ('2', 'two')


def is_vowel(char):
    """
    2.  Define a function named is_vowel. It should return True if the passed 
    string is a vowel, False otherwise.
    
    >>> is_vowel('A')
    True
    >>> is_vowel('a')
    True
    >>> is_vowel('B')
    False
    >>> is_vowel('b')
    False
    >>> is_vowel('y')
    Maybe
    False
    >>> is_vowel('3')
    False
    """
    test = char[0].lower()
    if test == 'y':
        print('Maybe')

    return test in 'aeiou'


def is_consonant(char):
    """
    3.  Define a function named is_consonant. It should return True if the 
    passed string is a consonant, False otherwise. Use your is_vowel function 
    to accomplish this.
    
    >>> is_consonant('A')
    False
    >>> is_consonant('a')
    False
    >>> is_consonant('B')
    True
    >>> is_consonant('b')
    True
    >>> is_consonant('y')
    Maybe
    True
    >>> is_consonant('3')
    False
    """
    test = char[0].lower()
    if test.isalpha():
        return is_vowel(test) == False
    else:
        return False




def return_word(chars):
    """
    4.  Define a function that accepts a string that is a word. The function 
    should capitalize the first letter of the word if the word starts with a 
    consonant.

    >>> return_word('word')
    'Word'
    >>> return_word('yard')
    Maybe
    'Yard'
    >>> return_word('award')
    'award'
    """
    if is_consonant(chars):
        return chars.capitalize() 
    else:
        return chars


def calculate_tip(check_amount, tip_percent=.2, tax_amount=0, round_to_dollar=0):
    """
    5.  Define a function named calculate_tip. It should accept a tip percentage 
    (a number between 0 and 1) and the bill total, and return the amount to 
    tip.

    WHAT I DID:
    Calculates tip based on check amount and target tip percentage. Allows 
    choice of tip percentage (defaults to .2 - 20%), removal of tax from the 
    tip calculation, and the ability to round the final payment up to a set 
    dollar multiple (e.g. nearest whole dollar, nearest $5, nearest $10) (or 
    down if less than 10% of the initially-calculated tip)
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
    if __name__ == '__main__':
        output_format = 'Check: {Check:>9.2f}\nTip: {Tip:>11.2f} (Base Tip: {BT:>6.2f})\nTotal: {Total:>9.2f}'
        print(output_format.format(Check=check_amount, BT=base_tip_amount, \
            Tip=tip_amount, Total=pay_amount))
        if plus_round:
            print('final tip is {:.1f}%'.format(100*tip_amount/tippable_amount))
    return round(tip_amount, 2)


# to_tip = calculate_tip(53.42,.25,6.75,5)


def apply_discount(original_price, discount_percentage):
    """
    6.  Define a function named apply_discount. It should accept a original 
    price, and a discount percentage, and return the price after the discount 
    is applied.
    
    >>> apply_discount(100, .2)
    80.0
    >>> apply_discount(100, .25)
    75.0
    >>> apply_discount(1, .6666)
    0.33
    """
    return round(original_price * (1 - discount_percentage), 2)


def handle_commas(chars):
    """
    7.  Define a function named handle_commas. It should accept a string that 
    is a number that contains commas in it as input, and return a number as 
    output.
    >>> handle_commas('1,000,000')
    1000000.0
    >>> handle_commas('1,234.56')
    1234.56
    """
    return float(chars.replace(',', ''))


def get_letter_grade(n):
    """
    8.  Define a function named get_letter_grade. It should accept a number 
    and return the letter grade associated with that number (A-F).
    >>> 
    """
    grades = {
        'A': range(90, 101),
        'B': range(80, 90),
        'C': range(70, 80),
        'D': range(60, 70),
        'F': range(0, 60)
    }
    for grade_letter, grade_range in grades.items():
        if round(n) in grade_range:
            return grade_letter
    return 'ACK! No answer for ' + n + '%'




def remove_vowels(chars):
    """
    9.  Define a function named remove_vowels that accepts a string and returns a 
    string with all the vowels removed.

    >>> remove_vowels('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz')
    'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz'
    """
    for vowel in 'aeiouAEIOU':
        chars = chars.replace(vowel,'')

    return chars 


def normalize_name(target_name):
    """
    10. Define a function named normalize_name. It should accept a string and 
    return a valid python identifier, that is:
        * anything that is not a valid python identifier should be removed
        * leading and trailing whitespace should be removed
        * everything should be lowercase
        * spaces should be replaced with underscores
    
    for example:    
    >>> normalize_name('Name')
    'name'
    >>> normalize_name('First Name  ')
    'first_name'
    >>> normalize_name('% Completed')
    'completed'
    >>> normalize_name("7_how's this?")
    '_7_hows_this'
    """
    valid_chars = 'abcdefghijklmnopqrstuvwxyz0123456789_ '
    in_process_name = target_name.lower()
    name_list = []
    new_name = ''
    for test in in_process_name:
        if test in valid_chars:
            name_list.append(test)
    new_name = ''.join(name_list).strip().replace(' ','_')
    if not new_name.isidentifier():
        new_name = '_' + new_name
    #if new_name == target_name:
    #    print('No change needed to [{}]'.format(target_name))
    #else:
    #    print('[{}] becomes [{}]'.format(target_name,new_name))
    return new_name


def cumsum(list):
    """
    11. Write a function named cumsum that accepts a list of numbers and returns a 
        list that is the cumulative sum of the numbers in the list.
     
    >>> cumsum([1, 1, 1])
    [1, 2, 3]
    >>> cumsum([1, 2, 3, 4])
    [1, 3, 6, 10]
    """
    runsum = 0
    sumrun = []
    for item in list:
        runsum = runsum + item
        sumrun.append(runsum)
    return sumrun  


"""
Bonii
"""



"""
1.  Create a function named twelveto24. It should accept a string in the 
    format 10:45am or 4:30pm and return a string that is the representation of 
    the time in a 24-hour format. Bonus write a function that does the opposite.
"""

def twelveto24(time_12):
    hour_value = int(time_12[:-5])
    minute_value = int(time_12[-4:-2])
    is_pm = time_12.lower().endswith('pm')
    if is_pm:
        hour_value = hour_value + 12 
    if hour_value == 24:
        hour_value = 0 
    time_24 = '{H:02d}:{M:02d}'.format(H=hour_value, M=minute_value)
    print ('{} becomes {}'.format(time_12, time_24))
    return time_24


def twelvefrom24(time_24):
    hour_value = int(time_24[:-3])
    minute_value = int(time_24[-2:])
    am_pm = 'PM' if hour_value > 11 else 'AM'
    if hour_value > 11:
        hour_value = hour_value - 12
    if hour_value == 0:
        hour_value = 12 
    time_12 = '{H:d}:{M:02d}{AP}'.format(H=hour_value, M=minute_value,AP=am_pm)
    print ('{} becomes {}'.format(time_24, time_12))
    return time_12


"""
2.  Create a function named col_index. It should accept a spreadsheet column 
    name, and return the index number of the column.
        col_index('A') returns 1
        col_index('B') returns 2
        col_index('AA') returns 27
"""

check_str = 'abcdefghijklmnopqrstuvwxyz'

def col_index(col_ltrs):
    flip_ltrs = reversed(col_ltrs.lower())
    on_idx = 0
    run_tot = 0
    for ltr in flip_ltrs:
        ltr_num = check_str.find(ltr) + 1
        ltr_val = ltr_num * (26 ** on_idx)
        on_idx += 1
        run_tot += ltr_val
    print(col_ltrs, run_tot, '\n')
    return run_tot
