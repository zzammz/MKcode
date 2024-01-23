

import inspect
import sys

# ========================= common
def log_trace(func_name):
    print ("\n----- " + func_name + "() -----")
    #print (inspect.stack()[1][3])
    #frame = inspect.currentframe()
    #print (inspect.getframeinfo(frame).function)
    #print(inspect.getframeinfo(inspect.currentframe()).function)
    return



def while_loop():
    log_trace("while_loop")

    print ("")
    print ("-- while")
    count = 0
    while count < 5:
        print(count)
        count = count + 1

    count = 0
    while count < 5:
        print(count)
        count = count + 1
        if (count == 3):
            break

    count = 0
    while count < 5:
        if count == 3:
            count = count + 1
            continue
        print(count)
        count = count + 1
    return

def for_loop():
    log_trace("for_loop")

    print("")
    print("-- for")

    language = 'Python'
    for letter in language:
        print(letter)

    for i in range(len(language)):
        print(language[i])

    numbers = (0, 1, 2, 3, 4, 5)
    for number in numbers:
        print(number)

    print("")
    print("-- fictionary looping")
    person = {
        'first_name': 'Jim',
        'last_name': 'Halpert',
        'age': 250,
        'country': 'US',
        'is_marred': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
    }
    for key in person:
        print(key)

    for key, value in person.items():
        print(key, value)  # this way we get both keys and values printed out

    print("")
    print("-- set")
    it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
    for company in it_companies:
        print(company)

    numbers = (0, 1, 2, 3, 4, 5)
    for number in numbers:
        print(number)
        if number == 3:
            break

    numbers = (0, 1, 2, 3, 4, 5)
    for number in numbers:
        print(number)
        if number == 3:
            continue
        if number != 5:
            print('Next number should be ', number + 1)
        else:
            print("loop's end")  # for short hand conditions need both if and else statements
    print('outside the loop')

    return


def range_func():
    log_trace("range_func")

    print("")
    print("-- range")
    lst = list(range(11))
    print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
    print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    lst = list(range(0,11,2))
    print(lst) # [0, 2, 4, 6, 8, 10]
    st = set(range(0,11,2))
    print(st) #  {0, 2, 4, 6, 8, 10}

    for number in range(11):
        print(number)  # prints 0 to 10, not including 11

    return

def nested_for_loop():
    log_trace("nested_for_loop")

    person = {
        'first_name': 'Jim',
        'last_name': 'Halpert',
        'age': 250,
        'country': 'US',
        'is_marred': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
    }
    for key in person:
        if key == 'skills':
            for skill in person['skills']:
                print(skill)
    return

def for_else():
    log_trace("for_else")

    for number in range(11):
        print(number)  # prints 0 to 10, not including 11  #
    else:
        print('The loop stops at', number)
    return


def loop_pass():
    log_trace("loop_pass")
    for number in range(6):
        pass
    return


# ========================= main
while_loop()
for_loop()
range_func()
nested_for_loop()
for_else()
loop_pass()

