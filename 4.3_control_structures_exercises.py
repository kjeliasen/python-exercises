
# Exercises
"""
    Do your work for this exercise in a file named `4.3_control_structures_exercises.py`.
""" 


## Conditional Basics


""" 
    1a) prompt the user for a day of the week, print out whether the day is 
        Monday or not
    1b) prompt the user for a day of the week, print out whether the day is 
        a weekday or a weekend
""" 

days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

weekday_days = days[:5]
weekend_days = days[5:]

output_format_1 = '{emphasis} {for_use} {use_is} a {kind}.'

clauses = {
    True: ('Yeehaw!', 'sure is'),
    False: ('Shucks.', 'ain\'t')
}


def day_is_weekend(day):
    return day in weekend_days


def day_is_day(day):
    return day in weekday_days


def get_user_day():
    user_input_day = input('Enter a galldanged day: ').capitalize()
    bailout = 0
    while user_input_day not in days:
        print(f"I said a galldanged day, dammit! {user_input_day} ain't no day!")
        if bailout < 3:
            user_input_day = input('Enter a real galldanged day: ').capitalize()
            bailout += 1
        else:
            user_input_day = 'Tuesday'
            print('Screw it. We\'re going with ' + user_input_day)
    return user_input_day.capitalize()


def day_is_monday(day):
    return day == days[0]


def report(kind, day, fn):
    c = clauses[fn(day)]
    print(output_format_1.format(kind=kind, emphasis=c[0], for_use=day, use_is=c[1]))


def do_tests(day):
    report('Monday', day, day_is_monday)
    report('weekday', day, day_is_day)
    report('weekend', day, day_is_weekend)


day = do_tests(get_user_day())

 
""" 
1c) create variables and make up values for
    - the number of hours worked in one week
    - the hourly rate
    - how much the week's paycheck will be
    - write the python code that calculates the weekly paycheck. You get paid 
    time and a half if you work more than 40 hours
"""

output_format_1c = '{wage_type:<15s} | {hours:>7.2f} | {dollars:>10.2f}'


def output_1c(wage_type,hours,dollars):
    print(output_format_1c.format(wage_type=wage_type, hours=hours, dollars=dollars))


def run_pay_report():
    output_1c('Straight Time',hours_st,pay_for_hours_st)
    output_1c('Overtime',hours_ot,pay_for_hours_ot)
    output_1c('TOTAL',hours_worked_in_week,total_pay)
    

hours_worked_in_week = 43
hourly_rate = 7.25
hours_st = min(hours_worked_in_week, 40)
hours_ot = max(hours_worked_in_week - hours_st, 0)
pay_for_hours_st = hours_st * hourly_rate
pay_for_hours_ot = hours_ot * hourly_rate * 1.5
total_pay = pay_for_hours_st + pay_for_hours_ot
hours_st

run_pay_report()


## Loop Basics


### While


def loop_it_gt(start_with,end_with,increment):
    test_val = start_with
    while test_val > end_with:
        print(test_val)
        test_val += increment


def loop_it_lt(start_with,end_with,increment):
    test_val = start_with
    while test_val < end_with:
        print(test_val)
        test_val += increment


def loop_it(start_with,end_with,increment):
    if increment > 0 and end_with > start_with:
        loop_it_lt(start_with,end_with,increment)
    elif increment < 0 and end_with < start_with:
        loop_it_gt(start_with,end_with,increment)
    else:
        print('Infinite Loop')


def loop_it_exp(start_with,end_with,exponent):
    test_val = start_with
    while test_val < end_with:
        print(test_val)
        test_val = test_val ** exponent


""" 
    2. Create an integer variable i with a value of 5.

    Create a while loop that runs so long as i is less than or equal to 15
    Each loop iteration, output the current value of i, then increment i by one.
    Your output should look like this:

    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
""" 
i = 5
loop_it(i,15.1,1)

"""
    Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
"""

loop_it(0,100.1,2)

"""
    Alter your loop to count backwards by 5's from 100 to -10.
"""

loop_it(100,-10.1,-5)

"""
    Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:

    2
    4
    16
    256
    65536

"""

loop_it_exp(2,1000000,2)


"""
    Write a loop that uses print to create the output shown below.

    100
    95
    90
    85
    80
    75
    70
    65
    60
    55
    50
    45
    40
    35
    30
    25
    20
    15
    10
    5
"""

loop_it(100,4,-5)


### For Loops

"""
    Write some code that prompts the user for a number, then shows a multiplication 
    table up through 10 for that number.

    For example, if the user enters 7, your program should output:

    7 x 1 = 7
    7 x 2 = 14
    7 x 3 = 21
    7 x 4 = 28
    7 x 5 = 35
    7 x 6 = 42
    7 x 7 = 49
    7 x 8 = 56
    7 x 9 = 63
    7 x 10 = 70
"""

output_format_2c = "{mult_num:>3} x {by_num:>3} = {yields_num:>4}"


def multiply_loop(mult_num, run_count):
    for on_num in range(1, run_count+1):
        product = int(mult_num) * on_num
        print(output_format_2c.format(mult_num=mult_num,by_num=on_num,yields_num=product))

multiply_loop(input('Gimmie a number: '),10)


"""
    Create a for loop that uses print to create the output shown below.


    1
    22
    333
    4444
    55555
    666666
    7777777
    88888888
    999999999
"""

for i in range(1, 10):
    o = str(i) * int(i)
    print(o)


### break and continue

"""
    Prompt the user for an odd number between 1 and 50. 
    Use a loop and a break statement to continue prompting the user if they 
    enter invalid input. (Hint: use the isdigit method on strings to determine 
    this). Use a loop and the continue statement to output all the odd numbers 
    between 1 and 50, except for the number the user entered.

    Your output should look like this:

    Number to skip is: 27

    Here is an odd number: 1
    Here is an odd number: 3
    Here is an odd number: 5
    Here is an odd number: 7
    Here is an odd number: 9
    Here is an odd number: 11
    Here is an odd number: 13
    Here is an odd number: 15
    Here is an odd number: 17
    Here is an odd number: 19
    Here is an odd number: 21
    Here is an odd number: 23
    Here is an odd number: 25
    Yikes! Skipping number: 27
    Here is an odd number: 29
    Here is an odd number: 31
    Here is an odd number: 33
    Here is an odd number: 35
    Here is an odd number: 37
    Here is an odd number: 39
    Here is an odd number: 41
    Here is an odd number: 43
    Here is an odd number: 45
    Here is an odd number: 47
    Here is an odd number: 49
"""

odd_nums = [x for x in range(50) if x % 2 == 1]


def odd_number_loop(start_at, end_at):
    for on_num in range(start_at, end_at + 1, 2):
        print(f'Here is an odd integer:{on_num:>3}')

def check_user_number():
    user_input = input('Gimmie an odd integet less than 50: ')
    
    while True:
        if user_input.isdigit() == False:
            print(f'{user_input} ain\'t no integer')
            break

        user_input = int(user_input)
        
        if user_input not in odd_nums:
            print(f'{user_input} isn\'t very odd at all')
            break
            
        if user_input > 1:
            odd_number_loop(1, user_input - 2)

        print(f'Yikes! Skipping number:{user_input:>3}')

        if user_input < 49:
            odd_number_loop(user_input + 2, 49)
            
        user_input = input('Gimmie another odd integer less than 50:')

        
check_user_number()


"""
    The input function can be used to prompt for input and use that input in 
    your python code. Prompt the user to enter a positive number and write a 
    loop that counts from 0 to that number. 
    (Hints: first make sure that the value the user entered is a valid number, 
    also note that the input function returns a string, so you'll need to 
    convert this to a numeric type.)
"""

def print_count_to_number(start_at, end_at, increment):
    count_out = [print(num) for num in range(start_at, end_at, increment)]


def count_to_user_number():
    user_input = input('Gimmie an positive integer: ')
    
    while True:
        if user_input.isdigit() == False:
            print(f'{user_input} ain\'t no integer')
            break

        user_int = int(user_input)
        
        if user_int > 0:
            print_count_to_number(0, user_int+1, 1)
            
        user_input = input('Gimmie another positive integer: ')

        
count_to_user_number()
 

"""
    Write a program that prompts the user for a positive integer. Next write a 
    loop that prints out the numbers from the number the user entered down to 1.
"""

### Fizzbuzz
""" 
One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

Write a program that prints the numbers from 1 to 100.
For multiples of three print "Fizz" instead of the number
For the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
"""


for num in range(1, 101):
    fb = ''
    if num % 3 == 0:
        fb += 'Fizz'
    if num % 5 == 0:
        fb += 'Buzz'
    if not fb:
        fb = num
    print(fb)


### Display a table of powers.
"""
Prompt the user to enter an integer.
Display a table of squares and cubes from 1 to the value entered.
Ask if the user wants to continue.
Assume that the user will enter valid data.
Only continue if the user agrees to.

Example Output
 
    What number would you like to go up to? 5

 
    Here is your table!
 
    number | squared | cubed
    ------ | ------- | -----
    1      | 1       | 1
    2      | 4       | 8
    3      | 9       | 27
    4      | 16      | 64
    5      | 25      | 125
"""
### Bonus: Research python's format string specifiers to align the table

top_output_format = "{col_num:>8s} | {col_square:>8s} | {col_cube:>8s}"
lbl_num = '{:<8s}'.format('number')
lbl_square = '{:<8s}'.format('squared')
lbl_cube = '{:<8s}'.format('cubed')
lbl_fill = '{:-<8s}'.format('')

def output_table_of_powers(upto_number):
    print('\nTable for {}\n'.format(upto_number))
    print(top_output_format.format(col_num=lbl_num, col_square=lbl_square, col_cube=lbl_cube))
    print(top_output_format.format(col_num=lbl_fill, col_square=lbl_fill, col_cube=lbl_fill))
    for num in range(1, upto_number + 1):
        print(top_output_format.format(col_num=str(num), col_square=str(num **2), col_cube=str(num ** 3)))

def get_user_number_for_table():
    go_on = 'Y'
    
    while go_on == 'Y':
        user_input = input('Gimmie a positive integer to power up: ')
        
        if user_input.isdigit() == False:
            print(f'{user_input} ain\'t no positive integer. How\'s about 5?')
            user_input = 5

        user_int = int(user_input)

        if user_int > 20:
            print('Sorry, I ain\'t countin\' that high. How\'s about 20?')
            user_int = 20

        if user_int < 3:
            print('Don\'t wanna go that low. How\'s about 3?')
            user_int = 3

        output_table_of_powers(user_int)
        
        go_on = input('Wanna try again? (Y/N) ').upper()
        

get_user_number_for_table()
         

"""
    Convert given number grades into letter grades.
    
    Prompt the user for a numerical grade from 0 to 100.
    Display the corresponding letter grade.
    Prompt the user to continue.
    Assume that the user will enter valid integers for the grades.
    The application should only continue if the user agrees to.
    Grade Ranges:
    
    A : 100 - 88
    B : 87 - 80
    C : 79 - 67
    D : 66 - 60
    F : 59 - 0

    Bonus
    
    Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).
    Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
    
    Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.
    """

