

# ========================= common
def log_trace(func_name):
    print ("\n--- " + func_name + "()")
    #print (inspect.stack()[1][3])
    #frame = inspect.currentframe()
    #print (inspect.getframeinfo(frame).function)
    #print(inspect.getframeinfo(inspect.currentframe()).function)
    return

def solution(src):
    longest_word = ""
    splitList = src.split()

    for item in splitList:
        if len(item) >= len(longest_word):
            longest_word = item
    return longest_word


# ========================= main
thesentence = "hello darkness my old friend I have come to talk with you again"

print ("the sentence: [" + thesentence + "]")
print ("longest word: [" + solution(thesentence) + "]")

