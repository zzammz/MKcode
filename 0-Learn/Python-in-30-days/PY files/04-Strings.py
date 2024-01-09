

import inspect
import sys

# ========================= common
def log_trace(func_name):
    print ("\n--- " + func_name + "()")
    #print (inspect.stack()[1][3])
    #frame = inspect.currentframe()
    #print (inspect.getframeinfo(frame).function)
    #print(inspect.getframeinfo(inspect.currentframe()).function)
    return

def creating_a_string():
    log_trace("creating_a_string")
    letter = 'P'  # A string could be a single character or a bunch of texts
    print(letter)  # P
    print(len(letter))  # 1
    greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
    print(greeting)  # Hello, World!
    print(len(greeting))  # 13
    sentence = "I hope you are having some fun"
    print(sentence)

    multiline_string = '''I am a teacher and enjoy teaching.
    I didn't find anything as rewarding as empowering people.
    That is why I fried mangoes.'''
    print(multiline_string)

    # Another way of doing the same thing
    multiline_string = """I am a teacher and enjoy teaching.
    I didn't find anything as rewarding as empowering people.
    That is why I fried mangoes."""
    print(multiline_string)

    return

def string_concatenation():
    log_trace("string_concatenation")
    first_name = 'Jim'
    last_name = 'H'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)  # Jim H

    # Checking the length of a string using len() built-in function
    print(len(first_name))  # 8
    print(len(last_name))  # 7
    print(len(first_name) > len(last_name))  # True
    print(len(full_name))  # 16
    return


def escape_sequences():
    log_trace("escape_sequences")
    print('I hope you are having fun.\nAre you ?')  # line break
    print('Days\tTopics\tExercises')  # adding tab space or 4 spaces
    print('Day 1\t5\t\t5')
    print('Day 2\t6\t\t20')
    print('Day 3\t5\t\t23')
    print('Day 4\t1\t\t35')
    print('This is a backslash  symbol (\\)')  # To write a backslash
    print('In every programming language it starts with \"Hello, World!\"')
    return

def string_formatting():
    log_trace("string_formatting")
    # Strings only
    first_name = 'Jim'
    last_name = 'H'
    language = 'Python'
    formated_string = 'I am %s %s. I teach %s' % (first_name, last_name, language)
    print(formated_string)

    # Strings  and numbers
    radius = 10
    pi = 3.14
    area = pi * radius ** 2
    formated_string = 'The area of circle with a radius %d is %.2f.' % (radius, area)  # 2 refers the 2 significant digits after the point

    python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']
    formated_string = 'The following are python libraries:%s' % (python_libraries)
    fruits_list = [ "apple", "cherry", "banana"]
    fruit_str = "I like these fruits: %s" %(fruits_list)
    print(fruit_str)
    print(formated_string)

    #new style with python 3
    first_name = 'Jim'
    last_name = 'H'
    language = 'Python'
    formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
    print(formated_string)
    a = 4
    b = 3

    print('{} + {} = {}'.format(a, b, a + b))
    print('{} - {} = {}'.format(a, b, a - b))
    print('{} * {} = {}'.format(a, b, a * b))
    print('{} / {} = {:.2f}'.format(a, b, a / b))  # limits it to two digits after decimal
    print('{} % {} = {}'.format(a, b, a % b))
    print('{} // {} = {}'.format(a, b, a // b))
    print('{} ** {} = {}'.format(a, b, a ** b))

    # Strings  and numbers
    radius = 10
    pi = 3.14
    area = pi * radius ** 2
    formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area)  # 2 digits after decimal
    print(formated_string)

    # String Interpolation / f-Strings (Python 3.6+)
    a = 4
    b = 3
    """
    print(f'{a} + {b} = {a + b}')
    print(f'{a} - {b} = {a - b}')
    print(f'{a} * {b} = {a * b}')
    print(f'{a} / {b} = {a / b:.2f}')
    print(f'{a} % {b} = {a % b}')
    print(f'{a} // {b} = {a // b}')
    print(f'{a} ** {b} = {a ** b}')
    """
    return

def string_as_sequence_of_chars():
    log_trace("string_as_sequence_of_chars")

    # unpacking
    language = 'Python'
    a, b, c, d, e, f = language  # unpacking sequence characters into variables
    print(a)  # P
    print(b)  # y
    print(c)  # t
    print(d)  # h
    print(e)  # o
    print(f)  # n

    # accessing by index
    language = 'Python'
    first_letter = language[0]
    print(first_letter)  # P
    second_letter = language[1]
    print(second_letter)  # y
    last_index = len(language) - 1
    last_letter = language[last_index]
    print(last_letter)  # n

    # from right
    language = 'Python'
    last_letter = language[-1]
    print(last_letter)  # n
    second_last = language[-2]
    print(second_last)  # o

    # slice string into substrings
    language = 'Python'
    first_three = language[0:3]  # starts at zero index and up to 3 but not include 3
    print(first_three)  # Pyt
    last_three = language[3:6]
    print(last_three)  # hon
    # Another way
    last_three = language[-3:]
    print(last_three)  # hon
    last_three = language[3:]
    print(last_three)  # hon

    # reversing a string
    greeting = 'Hello, World!'
    print(greeting[::-1])  # !dlroW ,olleH

    # skipping chars while slicing
    language = 'Python'
    pto = language[0:6:2]  #
    print(pto)  # Pto

    return

def string_methods():
    log_trace("string_methods")

    # capitalize(): Converts the first character of the string to capital letter
    challenge = 'thirty days of night'
    print(challenge.capitalize())  # 'Thirty days of night'

    # count(): returns occurrences of substring in string, count(substring, start=.., end=..).
    # The start is a starting indexing for counting and end is the last index to count.
    challenge = 'thirty days of python'
    print(challenge.count('y'))  # 3
    print(challenge.count('y', 7, 14))  # 1,
    print(challenge.count('th'))  # 2`

    # endswith(): Checks if a string ends with a specified ending
    challenge = 'thirty days of python'
    print(challenge.endswith('on'))  # True
    print(challenge.endswith('tion'))  # False

    # expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
    challenge = 'thirty\tdays\tof\tnight'
    print(challenge.expandtabs())
    print(challenge.expandtabs(10))

    # find(): Returns the index of the first occurrence of a substring, if not found returns -1
    challenge = 'thirty days of python'
    print(challenge.find('y'))  # 5
    print(challenge.find('th'))  # 0

    # rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
    challenge = 'thirty days of python'
    print(challenge.rfind('y'))  # 16
    print(challenge.rfind('th'))  # 17

    # format(): formats string into a nicer output
    first_name = 'Jim'
    last_name = 'Halpert'
    age = 250
    job = 'teacher'
    country = 'Finland'
    sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job,
                                                                                country)
    print(sentence)  # I am Jim H. I am 250 years old. I am a salesman. I live in Scranton.

    radius = 10
    pi = 3.14
    area = pi * radius ** 2
    result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
    print(result)  # The area of a circle with radius 10 is 314

    # index(): Returns the lowest index of a substring,
    # additional arguments indicate starting and ending index (default 0 and string length - 1).
    # If the substring is not found it raises a valueError.
    challenge = 'thirty days of python'
    sub_string = 'da'
    print(challenge.index(sub_string))  # 7
    #print(challenge.index(sub_string, 9))  # error


    # rindex(): Returns the highest index of a substring,
    # additional arguments indicate starting and ending index (default 0 and string length - 1)
    challenge = 'thirty days of python'
    sub_string = 'da'
    print(challenge.rindex(sub_string))  # 8
    print(challenge.rindex(sub_string, 9))  # error

    # isalnum(): Checks alphanumeric character
    challenge = 'ThirtyDaysPython'
    print(challenge.isalnum())  # True

    challenge = '30DaysPython'
    print(challenge.isalnum())  # True

    challenge = 'thirty days of python'
    print(challenge.isalnum())  # False, space is not an alphanumeric character

    challenge = 'thirty days of python 2019'
    print(challenge.isalnum())  # False

    # isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
    challenge = 'thirty days of python'
    print(challenge.isalpha())  # False, space is once again excluded
    challenge = 'ThirtyDaysPython'
    print(challenge.isalpha())  # True
    num = '123'
    print(num.isalpha())  # False

    # isdecimal(): Checks if all characters in a string are decimal (0-9)
    challenge = 'thirty days of python'
    print(challenge.isdecimal())  # False
    challenge = '123'
    print(challenge.isdecimal())  # True
    challenge = '\u00B2'
    print(challenge.isdigit())  # False
    challenge = '12 3'
    print(challenge.isdecimal())  # False, space not allowed


    # isdigit(): Checks if all chars in a string are numbers (0-9 and some other unicode chars for numbers)
    challenge = 'Thirty'
    print(challenge.isdigit())  # False
    challenge = '30'
    print(challenge.isdigit())  # True
    challenge = '\u00B2'
    print(challenge.isdigit())  # True

    #isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accept more symbols like %)
    num = '10'
    print(num.isnumeric())  # True
    num = '\u00BD'
    print(num.isnumeric())  # True
    num = '10.5'
    print(num.isnumeric())  # False

    # isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
    challenge = '30DaysOfPython'
    print(challenge.isidentifier())  # False, because it starts with a number
    challenge = 'thirty_days_of_python'
    print(challenge.isidentifier())  # True

    # islower(): Checks if all alphabet characters in the string are lowercase
    challenge = 'thirty days of python'
    print(challenge.islower())  # True
    challenge = 'Thirty days of python'
    print(challenge.islower())  # False

    # isupper(): Checks if all alphabet characters in the string are uppercase
    hallenge = 'thirty days of python'
    print(challenge.isupper())  # False
    challenge = 'THIRTY DAYS OF PYTHON'
    print(challenge.isupper())  # True

    #join(): Returns a concatenated string
    web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
    result = ' '.join(web_tech)
    print(result)  # 'HTML CSS JavaScript React'

    web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
    result = '# '.join(web_tech)
    print(result)  # 'HTML# CSS# JavaScript# React'

    # strip(): Removes all given characters starting from the beginning and end of the string
    challenge = 'thirty days of pythoonnn'
    print(challenge.strip('noth'))  # 'irty days of py'

    # replace(): Replaces substring with a given string
    challenge = 'thirty days of python'
    print(challenge.replace('python', 'coding'))  # 'thirty days of coding'

    # split(): Splits the string, using given string or space as a separator
    challenge = 'thirty days of python'
    print(challenge.split())  # ['thirty', 'days', 'of', 'python']
    challenge = 'thirty, days, of, python'
    print(challenge.split(', '))  # ['thirty', 'days', 'of', 'python']

    # title(): Returns a title cased string
    challenge = 'thirty days of python'
    print(challenge.title())  # Thirty Days Of Python

    # swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
    challenge = 'thirty days of python'
    print(challenge.swapcase())  # THIRTY DAYS OF PYTHON
    challenge = 'Thirty Days Of Python'
    print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

    # startswith(): Checks if String Starts with the Specified String
    challenge = 'thirty days of python'
    print(challenge.startswith('thirty'))  # True

    challenge = '30 days of python'
    print(challenge.startswith('thirty'))  # False

    return

# ========================= main

#creating_a_string()
#string_concatenation()
escape_sequences()
string_formatting()
#string_as_sequence_of_chars()
#string_methods()


