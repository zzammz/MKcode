"""
Given two strings, find the number of common characters between them.

Example

For `s1 = "aabcc"` and `s2 = "adcaa"`, the output should be  
`solution(s1, s2) = 3`.

Strings have `3` common characters - `2` "a"s and `1` "c".

Input/Output

-   **[execution time limit] 4 seconds (py3)**
    
-   **[input] string s1**
    
    A string consisting of lowercase English letters.
    
    _Guaranteed constraints:_  
    `1 ≤ s1.length < 15`.
    
-   **[input] string s2**
    
    A string consisting of lowercase English letters.
    
    _Guaranteed constraints:_  
    `1 ≤ s2.length < 15`.
    
-   **[output] integer**
"""

def solution(s1, s2):
    res = 0
    for p1 in s1:
        if p1 in s2:
            s2 = s2.replace(p1, '', 1)
            res += 1
            
    return res

    