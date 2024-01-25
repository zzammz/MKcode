
# see MakeArrayConsecutive2.txt for specs
# sort, then from min to mar, find how many missing pieces are needed to make it a series of +1
#For statues = [6, 2, 3, 8]`, the output should be
#`solution(statues) = 3`.
#Ratiorg needs statues of sizes 4, 5, 7
#

def mk_solution(statusList):
    missingCount = 0
    sortedList = sorted(statusList)
    iMin = sortedList[0]
    iMax = sortedList[-1]

    for ictr in range (iMin, iMax):
        iMin += 1
        if iMin not in sortedList:
            missingCount += 1

    return missingCount


def solution(statues):
    ans = 0
    # search min and max
    results_list = sorted(statues)
    min, max = results_list[0], results_list[-1]
    
    for i in range(min, max):
        min += 1
        if min not in statues:
            print (min)  #debug
            ans += 1
    return ans

# main
statues = [6, 2, 3, 8]
myresult = mk_solution(statues)
print ("count: " + str (myresult) )

