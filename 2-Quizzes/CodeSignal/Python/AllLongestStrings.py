"""
Given an array of strings, return another array containing all of its longest strings.

Example

For `inputArray = ["aba", "aa", "ad", "vcd", "aba"]`, the output should be  
`solution(inputArray) = ["aba", "vcd", "aba"]`.

Input/Output

-   **[execution time limit] 4 seconds (py3)**
    
-   **[input] array.string inputArray**
    
    A non-empty array.
    
    _Guaranteed constraints:_  
    `1 ≤ inputArray.length ≤ 10`,  
    `1 ≤ inputArray[i].length ≤ 10`.
    
-   **[output] array.string**
    
    Array of the longest strings, stored in the same order as in the `inputArray`.

"""



def solution(inputArray):
    max_value = max([len(i) for i in inputArray])
    return list(filter(lambda x: len(x) == max_value, inputArray))

