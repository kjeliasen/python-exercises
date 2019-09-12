#!/usr/bin/env python
# coding: utf-8

# In[5]:


days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

weekday_days = days[:5]
weekend_days = days[5:]

output_format = '{emphasis} {for_use} {use_is} a {kind}.'

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
    print(output_format.format(kind=kind, emphasis=c[0], for_use=day, use_is=c[1]))


def do_tests(day):
    report('Monday', day, day_is_monday)
    report('weekday', day, day_is_day)
    report('weekend', day, day_is_weekend)


day = do_tests(get_user_day())


# In[ ]:




