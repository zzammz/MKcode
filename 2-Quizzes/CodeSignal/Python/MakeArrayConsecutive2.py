
"""
Ratiorg got `statues` of _different_ sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by `1`. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

Example

For `statues = [6, 2, 3, 8]`, the output should be  
`solution(statues) = 3`.

Ratiorg needs statues of sizes `4`, `5` and `7`.

Input/Output

-   **[execution time limit] 4 seconds (py3)**
    
-   **[input] array.integer statues**
    
    An array of _distinct_ non-negative integers.
    
    _Guaranteed constraints:_  
    `1 ≤ statues.length ≤ 10`,  
    `0 ≤ statues[i] ≤ 20`.
    
-   **[output] integer**
    
    The minimal number of statues that need to be added to existing `statues` such that it contains every integer size from an interval `[L, R]` (for some `L, R`) and no other sizes.

"""



def solution(statues):
    ans = 0
    # search min and max
    results_list = sorted(statues)
    min, max = results_list[0], results_list[-1]
    
    for i in range(min, max):
        min += 1
        if min not in statues:
            ans += 1
    return ans

