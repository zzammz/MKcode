# MK utils

#import datetime
#from datetime import datetime
import time


def HelloWorld():
    print ("Hello, World!")


def addLog (strLog):
    #print(time.strftime("%x %X", ts)) ## 12/31/18 22:48:42
    #iso format - print(time.strftime("%c", ts))  ### Mon Dec 31 22:48:42 2018

    tmpTimestamp = time.gmtime()
    tmpstrTime = time.strftime("%Y-%m-%d %H.%M.%S", tmpTimestamp)
    print ("%s: %s" % (tmpstrTime, strLog))

