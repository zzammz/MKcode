  

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

def examples_print():
    log_trace("examples_print")
    print('Hello, World!')  # The text Hello, World! is an argument
    print('Hello', ',', 'World', '!')  # it can take multiple arguments, four arguments have been passed
    print(len('Hello, World!'))  # it takes only one argument
    return

def examples_variables():
    log_trace("examples_variables")
    first_name = 'Jim'
    last_name = 'Halpert'
    country = 'US'
    city = 'Scranton'
    age = 250
    is_married = True
    skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
    person_info = {
        'firstname': 'Jim',
        'lastname': 'Halpert',
        'country': 'US',
        'city': 'Scranton'
    }
    print('First name:', first_name) 
    print('First name length:', len(first_name))
    print('Last name: ', last_name)
    print('Last name length: ', len(last_name))
    print('Country: ', country)
    print('City: ', city)
    print('Age: ', age)
    print('Married: ', is_married)
    print('Skills: ', skills)
    print('Person information: ', person_info)

    print(first_name, last_name, country, age, is_married)
    print('First name:', first_name)
    print('Last name: ', last_name)
    print('Country: ', country)
    print('Age: ', age)
    print('Married: ', is_married)

    return

def examples_type():
    log_trace("examples_type")
    first_name = 'Jim'  # str
    last_name = 'Halpert'  # str
    country = 'US'  # str
    city = 'Scranton'  # str
    age = 250  # int, it is not my real age, don't worry about it

    # Printing out types
    print(type('Jim'))  # str
    print(type(first_name))  # str
    print(type(10))  # int
    print(type(3.14))  # float
    print(type(1 + 1j))  # complex
    print(type(True))  # bool
    print(type([1, 2, 3, 4]))  # list
    print(type({'name': 'Jim', 'age': 250, 'is_married': 250}))  # dict
    print(type((1, 2)))  # tuple
    print(type(zip([1, 2], [3, 4])))  # set
    print(type({"we", "are", "the", "world"})) #set
    return

def examples_type_casting():
    log_trace("examples_type_casting")
    # int to float
    num_int = 10
    print('num_int', num_int)  # 10
    num_float = float(num_int)
    print('num_float:', num_float)  # 10.0

    # float to int
    gravity = 9.81
    print(int(gravity))  # 9

    # int to str
    num_int = 10
    print(num_int)  # 10
    num_str = str(num_int)
    print(num_str)  # '10'

    # str to int or float
    num_str = '10.6'
    #print('num_int', int(num_str))  # 10
    print('num_float', float(num_str))  # 10.6

    # str to list
    first_name = 'Jim'
    print(first_name)  # 'Jim'
    first_name_to_list = list(first_name)
    print(first_name_to_list)  # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']

    return

# ========================= main

examples_print()
examples_variables()

examples_type()
examples_type_casting()





