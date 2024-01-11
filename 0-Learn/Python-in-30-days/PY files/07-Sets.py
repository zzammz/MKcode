

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



def set_basics():
    log_trace("set_basics")

    print ("")
    print ("-- set_basics")

    return


def xx(**kwargs):
    log_trace("xx")

    print("")
    print("-- x")
    # kwargs is a dict
    print(type(kwargs))

    # Printing dictionary items
    for key in kwargs:
        print("%s = %s" % (key, kwargs[key]))

    return

# ========================= main
#set_basics()

# Driver code
xx(name="geeks", ID="101", language="Python")
