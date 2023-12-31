
"""
wo arrays are called _similar_ if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays `a` and `b`, check whether they are _similar_.

Example

-   For `a = [1, 2, 3]` and `b = [1, 2, 3]`, the output should be  
    `solution(a, b) = true`.
    
    The arrays are equal, no need to swap any elements.
    
-   For `a = [1, 2, 3]` and `b = [2, 1, 3]`, the output should be  
    `solution(a, b) = true`.
    
    We can obtain `b` from `a` by swapping `2` and `1` in `b`.
    
-   For `a = [1, 2, 2]` and `b = [2, 1, 1]`, the output should be  
    `solution(a, b) = false`.
    
    Any swap of any two elements either in `a` or in `b` won't make `a` and `b` equal.
    

Input/Output

-   **[execution time limit] 4 seconds (py3)**
    
-   **[input] array.integer a**
    
    Array of integers.
    
    _Guaranteed constraints:_  
    `3 ≤ a.length ≤ 105`,  
    `1 ≤ a[i] ≤ 1000`.
    
-   **[input] array.integer b**
    
    Array of integers of the same length as `a`.
    
    _Guaranteed constraints:_  
    `b.length = a.length`,  
    `1 ≤ b[i] ≤ 1000`.
    
-   **[output] boolean**
    
    `true` if `a` and `b` are similar, `false` otherwise.
"""


def solution(a, b):
    change = -1
    count = 0
    for i in range(len(a)):
        if a[i] != b[i] and change != -1:
            if a[change]!=b[i] or b[change]!=a[i]:
                return False
                
        if a[i] != b[i] and change == -1:
            change = i
        
        if a[i] == b[i]:
            count += 1      
            
    return len(a)-2 == count or len(a) == count


   