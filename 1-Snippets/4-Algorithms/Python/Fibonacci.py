

# fibonacci - iterative
def fib_1(param_val):
    log_trace(inspect.getframeinfo(inspect.currentframe()).function)
    if param_val < 0:
        print ("incorrect value - cannot be less than 1")
        return

    prev_val = 0
    current_val = 1

    print(" {} ".format(0))
    if param_val == 1:
        return

    print(" {} ".format(1))
    if param_val == 2:
        return

    prev_val = current_val
    very_prev_val = 0

    for ictr in range (2, param_val):
        current_val = very_prev_val + prev_val
        very_prev_val = prev_val
        prev_val = current_val
        print (" {} ".format(current_val))
    return

# fibonacci - recursive
def fib_2(param_val):
    #log_trace(inspect.getframeinfo(inspect.currentframe()).function)
    if param_val < 0:
        print("incorrect value - cannot be less than 1")
        return
    elif param_val == 1:
        return 0
    elif param_val == 2:
        return 1
    else:
        return fib_2(param_val-1) + fib_2(param_val-2)



#--------- main
print ("=== fibonacci - iterative")
fib_1(5)
print ("")

print ("=== fibonacci - recursive")
print ("{}th fib num is: ".format(5) + str(fib_2(5)))

