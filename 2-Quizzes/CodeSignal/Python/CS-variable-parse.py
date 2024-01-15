

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


def find_in_list(mylist, find_value):
    find_pos = -1
    if find_value in mylist:
        find_pos = mylist.index(find_value)
    return find_pos


def solution2(src):
    returnValue = ""
    firstChar = ""
    lastChar = ""
    fullreturnvalue = ""

    mysplit = src.split(' ')

    for listitem in mysplit:
        #print ("\n100: word is: " + listitem)
        if( "_" in listitem):
            #print ("300: _ found")
            returnValue = ""
            firstChar = ""
            lastChar = ""
            if (listitem[0] == "_"):
                firstChar = "_"

            if (src[len(listitem) - 1] == "_"):
                lastChar = "_"

            splitList = listitem.split('_')
            #print ("301: ")
            #print (splitList)
            buildWord = ""

            #returnValue = splitList[0]

            firstWordPassed = False
            for ictr in range(0, len(splitList)):

                tmpword = ""
                if (splitList[ictr] == ""):
                    buildWord = buildWord + "_"
                else:
                    if (firstWordPassed):
                        tmpword = splitList[ictr].capitalize()
                    else:
                        tmpword = splitList[ictr]
                        firstWordPassed = True
                    buildWord = buildWord + tmpword
            #print ("101: [" + buildWord + "]")
            #print (buildWord)
            fullreturnvalue = fullreturnvalue + " " + buildWord
        else: # no _
            #print("400: _ not found")
            fullreturnvalue = fullreturnvalue + " " + listitem

        #print ("===response so far: [" + fullreturnvalue + "]")

    #print (fullreturnvalue)
    fullreturnvalue2 = fullreturnvalue
    if (fullreturnvalue[0] == " "):
        fullreturnvalue2 = fullreturnvalue[1:]

    return fullreturnvalue2



def test2():

    varTest = "_"
    print("#1: " + varTest)
    print ("[" + solution2(varTest) + "]\n")

    varTest = "this_is_something"
    print("#2: " + varTest)
    print("[" + solution2(varTest) + "]\n")

    varTest = "_this_is_something_"
    print("#3: " + varTest)
    print("[" + solution2(varTest) + "]\n")

    varTest = "this_is_something_"
    print("#4: " + varTest)
    print("[" + solution2(varTest) + "]\n")

    varTest = "This is the doc_string for _secret_fun"
    print("#5: " + varTest)
    print("[" + solution2(varTest) + "]\n")

    return



# ========================= main
test2()



