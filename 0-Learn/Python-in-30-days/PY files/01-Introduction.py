  

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

def examples_basic_print():
    log_trace("examples_basic_print")
    print(2 + 3)  # addition(+)
    print(3 - 1)  # subtraction(-)
    print(2 * 3)  # multiplication(*)
    print(3 / 2)  # division(/)
    print(3 ** 2)  # exponential(**)
    print(3 % 2)  # modulus(%)
    print(3 // 2)  # Floor division operator(//) 
    return

def examples_print():
    log_trace("examples_print")
    print('Hello, World!')  # The text Hello, World! is an argument
    print('Hello', ',', 'World', '!')  # it can take multiple arguments, four arguments have been passed
    print(len('Hello, World!'))  # it takes only one argument
    return

def examples_check_data_type():
    log_trace("examples_check_data_type")
    print(type(10))  # Int
    print(type(3.14))  # Float
    print(type(1 + 3j))  # Complex
    print(type('Jim'))  # String
    print(type([1, 2, 3]))  # List
    print(type({'name': 'Jim'}))  # Dictionary
    print(type({9.8, 3.14, 2.7}))  # Set
    print(type((9.8, 3.14, 2.7)))  # Tuple
    return

#

# ========================= main

examples_basic_print()
examples_print()
examples_check_data_type()





