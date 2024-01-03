"""
Given a rectangular matrix of characters, add a border of asterisks(`*`) to it.

Example

For

```
picture = ["abc",
           "ded"]
```

the output should be

```
solution(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
```

Input/Output

-   **[execution time limit] 4 seconds (py3)**
    
-   **[input] array.string picture**
    
    A non-empty array of non-empty equal-length strings.
    
    _Guaranteed constraints:_  
    `1 ≤ picture.length ≤ 100`,  
    `1 ≤ picture[i].length ≤ 100`.
    
-   **[output] array.string**
    
    The same matrix of characters, framed with a border of asterisks of width `1`.
"""


def solution(picture):
    length = len(picture)+2
    asterisk = len(picture[0])+2
    count = 0
    res = []
    for i in range(length):
        if i == 0 or i == length-1:
            res.append('*'*asterisk)
        else:
            res.append('*' +picture[count]+ '*')
            count += 1       
    return res

