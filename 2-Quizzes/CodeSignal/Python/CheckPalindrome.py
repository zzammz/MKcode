"""
Given the string, check if it is a [palindrome](keyword://palindrome).

Example

-   For `inputString = "aabaa"`, the output should be  
    `solution(inputString) = true`;
-   For `inputString = "abac"`, the output should be  
    `solution(inputString) = false`;
-   For `inputString = "a"`, the output should be  
    `solution(inputString) = true`.

Input/Output

-   **[execution time limit] 4 seconds (py3)**
    
-   **[input] string inputString**
    
    A non-empty string consisting of lowercase characters.
    
    _Guaranteed constraints:_  
    `1 ≤ inputString.length ≤ 105`.
    
-   **[output] boolean**
    
    `true` if `inputString` is a palindrome, `false` otherwise.

"""


def solution(inputString):
    rev = inputString[::-1]
    
    for i in range(len(inputString)): 
        if inputString[i] != rev[i]:
            return False
    return True

