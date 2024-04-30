

import inspect
import sys

# ========================= common
def log_trace(func_name):
    print ("\n\n========== " + func_name + "()")
    #print (inspect.stack()[1][3])
    #frame = inspect.currentframe()
    #print (inspect.getframeinfo(frame).function)
    #print(inspect.getframeinfo(inspect.currentframe()).function)
    return

def log_trace2(str_msg):
    print ("\n--- " + str_msg)
    return


def dict_basics():
    log_trace("dict_basics")

    print ("")
    log_trace2("creating")
    empty_dict = {}
    # Dictionary with data values
    dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
    print ("dct:")
    print (dct)

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
    print ("person:")
    print (person)


    log_trace2("getting length")
    print ("items in dct: ")
    print (len(dct))
    print ("items in person")
    print (len(person))


    log_trace2("accessing items in a dict")
    print ("accessing from dct")
    print(dct['key1'])  # value1
    print(dct['key4'])  # value4

    print ("\naccessing from person")
    print(person['first_name'])  # Jim
    print(person['country'])  # Halpert
    print(person['skills'])  # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
    print(person['skills'][0])  # JavaScript
    print(person['address']['street'])  # Space street
    #print(person['city'])  # Error

    print("\nusing 'get' to access from person")
    print(person.get('first_name'))  # Jim
    print(person.get('country'))  # Halpert
    print(person.get('skills'))  # ['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
    print(person.get('city'))  # None

    return


def adding_items():
    log_trace("adding_items")

    dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
    print (dct)
    dct['key5'] = 'value5'
    print(dct)

    print ("")
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
    print (person)
    person['job_title'] = 'Instructor'
    person['skills'].append('HTML')
    print(person)

    return


def modifying_items():
    log_trace("modifying_items")

    dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
    print (dct)
    dct['key1'] = 'value-one'
    print(dct)

    print ("")
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
    print (person)
    person['first_name'] = 'Michael'
    person['age'] = 252
    print(person)

    return


def checking_keys():
    log_trace("checking_keys")

    dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
    print('key2' in dct)  # True
    print('key5' in dct)  # False

    return


def removing_key_and_value_pairs():
    log_trace("removing_key_and_value_pairs")
    # pop(key): removes the item with the specified key name:
    # popitem(): removes the last item
    # del: removes an item with specified key name

    dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
    print (dct)
    dct.pop('key1')  # removes key1 item
    print(dct)

    dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
    print(dct)
    dct.popitem()  # removes the last item
    print(dct)
    del dct['key2']  # removes key2 item
    print(dct)

    print ("")
    person = {
        'first_name': 'Jim',
        'last_name': 'Halpert',
        'age': 250,
        'country': 'US',
        'is_married': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
    }
    print (person)
    person.pop('first_name')  # Removes the firstname item
    print(person)
    person.popitem()  # Removes the address item
    print(person)
    del person['is_married']  # Removes the is_married item
    print(person)

    return


def converting_dict_to_list():
    log_trace("converting_dict_to_list")

    log_trace2 ("get entire dict as list")
    dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
    print (dct)
    print(dct.items())  # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

    print ("")
    log_trace2("get all keys using keys()")
    dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
    print (dct)
    keys = dct.keys()
    print(keys)  # dict_keys(['key1', 'key2', 'key3', 'key4'])

    print("")
    log_trace2("get all values using values()")
    dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
    print(dct)
    values = dct.values()
    print(values)  # dict_values(['value1', 'value2', 'value3', 'value4'])

    return


def clearing_dict():
    log_trace("clearing_dict")

    dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
    print (dct)
    print(dct.clear())  # None
    print(dct)

    return


def deleting_dict():
    log_trace("deleting_dict")

    dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
    del dct

    return

# ========================= main
dict_basics()
adding_items()
modifying_items()
checking_keys()
removing_key_and_value_pairs()
converting_dict_to_list()
clearing_dict()
deleting_dict()

