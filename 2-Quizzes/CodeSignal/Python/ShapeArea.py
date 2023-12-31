"""
Below we will define an `n`-interesting polygon. Your task is to find the area of a polygon for a given `n`.

A `1`-interesting polygon is just a square with a side of length `1`. An `n`-interesting polygon is obtained by taking the `n - 1`-interesting polygon and appending `1`-interesting polygons to its rim, side by side. You can see the `1`-, `2`-, `3`- and `4`-interesting polygons in the picture below.

![](https://codesignal.s3.amazonaws.com/uploads/1664318501/area.png)

Example

-   For `n = 2`, the output should be  
    `solution(n) = 5`;
-   For `n = 3`, the output should be  
    `solution(n) = 13`.

Input/Output

-   **[execution time limit] 4 seconds (py3)**
    
-   **[input] integer n**
    
    _Guaranteed constraints:_  
    `1 ≤ n < 104`.
    
-   **[output] integer**
    
    The area of the `n`-interesting polygon.

"""



def solution(n):
    res, multi = 0, 1
    for i in range(1,n+1):
        res += multi * 2
        if i != n: multi += 2
    res -= multi  
    return res

