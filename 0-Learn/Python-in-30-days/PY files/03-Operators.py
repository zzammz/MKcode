

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

def examples_arithmetic_ops():
    log_trace("examples_arithmetic_ops")

    # integers
    print('Addition: ', 1 + 2)  # 3
    print('Subtraction: ', 2 - 1)  # 1
    print('Multiplication: ', 2 * 3)  # 6
    print('Division: ', 4 / 2)  # 2.0  Division in Python gives floating number
    print('Division: ', 6 / 2)  # 3.0
    print('Division: ', 7 / 2)  # 3.5
    print('Division without the remainder: ', 7 // 2)  # 3,  gives without the floating number or without the remaining
    print('Division without the remainder: ', 7 // 3)  # 2
    print('Modulus: ', 3 % 2)  # 1, Gives the remainder
    print('Exponentiation: ', 2 ** 3)  # 9 it means 2 * 2 * 2

    # float
    print('Floating Point Number, PI', 3.14)
    print('Floating Point Number, gravity', 9.81)
 
    # complex numbers
    print('Complex number: ', 1 + 1j)
    print('Multiplying complex numbers: ', (1 + 1j) * (1 - 1j))

    # Arithmetic operations and assigning the result to a variable
    a = 3  # a is a variable name and 3 is an integer data type
    b = 2  # b is a variable name and 3 is an integer data type
    total = a + b
    diff = a - b
    product = a * b
    division = a / b
    remainder = a % b
    floor_division = a // b
    exponential = a ** b

    print(total)
    print('a + b = ', total)
    print('a - b = ', diff)
    print('a * b = ', product)
    print('a / b = ', division)
    print('a % b = ', remainder)
    print('a // b = ', floor_division)
    print('a ** b = ', exponential)

    print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

    # formulas
    # Calculating area of a circle
    radius = 10  # radius of a circle
    area_of_circle = 3.14 * radius ** 2  # two * sign means exponent or power
    print('Area of a circle:', area_of_circle)

    # Calculating area of a rectangle
    length = 10
    width = 20
    area_of_rectangle = length * width
    print('Area of rectangle:', area_of_rectangle)

    # Calculating a weight of an object
    mass = 75
    gravity = 9.81
    weight = mass * gravity
    print(weight, 'N')  # Adding unit to the weight

    # Calculate the density of a liquid
    mass = 75  # in Kg
    volume = 0.075  # in cubic meter
    density = mass / volume  # 1000 Kg/m^3

    return

def examples_comparison_operators():
    log_trace("examples_comparison_operators")
    print(3 > 2)  # True, because 3 is greater than 2
    print(3 >= 2)  # True, because 3 is greater than 2
    print(3 < 2)  # False,  because 3 is greater than 2
    print(2 < 3)  # True, because 2 is less than 3
    print(2 <= 3)  # True, because 2 is less than 3
    print(3 == 2)  # False, because 3 is not equal to 2
    print(3 != 2)  # True, because 3 is not equal to 2
    print(len('mango') == len('avocado'))  # False
    print(len('mango') != len('avocado'))  # True
    print(len('mango') < len('avocado'))  # True
    print(len('milk') != len('meat'))  # False
    print(len('milk') == len('meat'))  # True
    print(len('tomato') == len('potato'))  # True
    print(len('python') > len('dragon'))  # False

    # Comparing something gives either a True or False
    print('True == True: ', True == True)
    print('True == False: ', True == False)
    print('False == False:', False == False)

    print('1 is 1', 1 is 1)  # True - because the data values are the same
    print('1 is not 2', 1 is not 2)  # True - because 1 is not 2
    print('A in Jim', 'A' in 'Jim')  # True - A found in the string
    print('B in Jim', 'B' in 'Jim')  # False - there is no uppercase B
    print('coding' in 'coding for all')  # True - because coding for all has the word coding
    print('a in an:', 'a' in 'an')  # True
    print('4 is 2 ** 2:', 4 is 2 ** 2)  # True
    return


def examples_logical_operators():
    print(3 > 2 and 4 > 3)  # True - because both statements are true
    print(3 > 2 and 4 < 3)  # False - because the second statement is false
    print(3 < 2 and 4 < 3)  # False - because both statements are false
    print('True and True: ', True and True)
    print(3 > 2 or 4 > 3)  # True - because both statements are true
    print(3 > 2 or 4 < 3)  # True - because one of the statements is true
    print(3 < 2 or 4 < 3)  # False - because both statements are false
    print('True or False:', True or False)
    print(not 3 > 2)  # False - because 3 > 2 is true, then not True gives False
    print(not True)  # False - Negation, the not operator turns true to false
    print(not False)  # True
    print(not not True)  # True
    print(not not False)  # False
    return


# ========================= main

examples_arithmetic_ops()
examples_comparison_operators()
examples_logical_operators()






