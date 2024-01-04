# USEFUL STUFF



============================================================================

> [!NOTE]
> ## Calculates the date of n days from the given date.

Use datetime.timedelta and the + operator to calculate the new datetime.datetime value after adding n days to d.
Omit the second argument, d, to use a default value of datetime.today().
from datetime import datetime, timedelta


```py
def add_days(n, d = datetime.today()):
  return d + timedelta(n)

from datetime import date

add_days(5, date(2020, 10, 25)) # date(2020, 10, 30)
add_days(-5, date(2020, 10, 25)) # date(2020, 10, 20)
```




============================================================================

> [!NOTE]
> ## Checks if all elements in a list are equal.

Use set() to eliminate duplicate elements and then use len() to check if length is 1.

```py
def all_equal(lst):
  return len(set(lst)) == 1


all_equal([1, 2, 3, 4, 5, 6]) # False
all_equal([1, 1, 1, 1]) # True

```

============================================================================

> [!NOTE]
> ## Checks if all the values in a list are unique.

Use set() on the given list to keep only unique occurrences.
Use len() to compare the length of the unique values to the original list.

```py
def all_unique(lst):
  return len(lst) == len(set(lst))

x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 2, 3, 4, 5]
all_unique(x) # True
all_unique(y) # False
```

============================================================================

> [!NOTE]
> ## Arithmetic progression

Generates a list of numbers in the arithmetic progression starting with the given positive integer and up to the specified limit.

Use range() and list() with the appropriate start, step and end values.

```py
def arithmetic_progression(n, lim):
  return list(range(n, lim + 1, n))

arithmetic_progression(5, 25) # [5, 10, 15, 20, 25]
```

============================================================================

> [!NOTE]
> ## Mapped list average


Calculates the average of a list, after mapping each element to a value using the provided function.

Use map() to map each element to the value returned by fn.
Use sum() to sum all of the mapped values, divide by len(lst).
Omit the last argument, fn, to use the default identity function.


```py
def average_by(lst, fn = lambda x: x):
  return sum(map(fn, lst), 0.0) / len(lst)


average_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda x: x['n'])
# 5.0
```


======================
Average


Calculates the average of two or more numbers.

Use sum() to sum all of the args provided, divide by len().

```py
def average(*args):
  return sum(args, 0.0) / len(args)


average(*[1, 2, 3]) # 2.0
average(1, 2, 3) # 2.0
```

==================
Bifurcate list based on function


Splits values into two groups, based on the result of the given filtering function.

Use a list comprehension to add elements to groups, based on the value returned by fn for each element.
If fn returns a truthy value for any element, add it to the first group, otherwise add it to the second group.

```py
def bifurcate_by(lst, fn):
  return [
    [x for x in lst if fn(x)],
    [x for x in lst if not fn(x)]
  ]

bifurcate_by(['beep', 'boop', 'foo', 'bar'], lambda x: x[0] == 'b')
# [ ['beep', 'boop', 'bar'], ['foo'] ]
```

==================
Bifurcate list based on values


Splits values into two groups, based on the result of the given filter list.

Use a list comprehension and zip() to add elements to groups, based on filter.
If filter has a truthy value for any element, add it to the first group, otherwise add it to the second group.


```py
def bifurcate(lst, filter):
  return [
    [x for x, flag in zip(lst, filter) if flag],
    [x for x, flag in zip(lst, filter) if not flag]
  ]

bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True])
# [ ['beep', 'boop', 'bar'], ['foo'] ]
```

==================
Binomial coefficient


Calculates the number of ways to choose k items from n items without repetition and without order.

Use math.comb() to calculate the binomial coefficient.


```py
from math import comb

def binomial_coefficient(n, k):
  return comb(n, k)
binomial_coefficient(8, 2) # 28

```


==================
Byte size of string

Returns the length of a string in bytes.

Use str.encode() to encode the given string and return its length.

```py
def byte_size(s):
  return len(s.encode('utf-8'))

byte_size('😀') # 4
byte_size('Hello World') # 11
```


==================
Camelcase string
Converts a string to camelcase.

Use re.sub() to replace any - or _ with a space, using the regexp r"(_|-)+".
Use str.title() to capitalize the first letter of each word and convert the rest to lowercase.
Finally, use str.replace() to remove spaces between words.

```py
from re import sub

def camel(s):
  s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
  return ''.join([s[0].lower(), s[1:]])


camel('some_database_field_name') # 'someDatabaseFieldName'
camel('Some label that needs to be camelized')
# 'someLabelThatNeedsToBeCamelized'
camel('some-javascript-property') # 'someJavascriptProperty'
camel('some-mixed_string with spaces_underscores-and-hyphens')
# 'someMixedStringWithSpacesUnderscoresAndHyphens'
```


==================
Capitalize every word

Capitalizes the first letter of every word in a string.

Use str.title() to capitalize the first letter of every word in the string.

```py
def capitalize_every_word(s):
  return s.title()

capitalize_every_word('hello world!') # 'Hello World!'
```


==================
Capitalize string

Capitalizes the first letter of a string.

Use list slicing and str.upper() to capitalize the first letter of the string.
Use str.join() to combine the capitalized first letter with the rest of the characters.
Omit the lower_rest parameter to keep the rest of the string intact, or set it to True to convert to lowercase.

```py
def capitalize(s, lower_rest = False):
  return ''.join([s[:1].upper(), (s[1:].lower() if lower_rest else s[1:])])

capitalize('fooBar') # 'FooBar'
capitalize('fooBar', True) # 'Foobar'
```


==================
Casts the provided value as a list if it's not one.

Use isinstance() to check if the given value is enumerable.
Return it by using list() or encapsulated in a list accordingly.

```py
def cast_list(val):
  return list(val) if isinstance(val, (tuple, list, set, dict)) else [val]


cast_list('foo') # ['foo']
cast_list([1]) # [1]
cast_list(('foo', 'bar')) # ['foo', 'bar']
```

=======================
Celsius to Fahrenheit


Converts Celsius to Fahrenheit.

Follow the conversion formula F = 1.8 * C + 32.

```py
def celsius_to_fahrenheit(degrees):
  return ((degrees * 1.8) + 32)

celsius_to_fahrenheit(180) # 356.0
```

=======================
Check property

Creates a function that will invoke a predicate function for the specified property on a given dictionary.

Return a lambda function that takes a dictionary and applies the predicate function, fn to the specified property.

```py
def check_prop(fn, prop):
  return lambda obj: fn(obj[prop])


check_age = check_prop(lambda x: x >= 18, 'age')
user = {'name': 'Mark', 'age': 18}
check_age(user) # True
```


=======================
Split list into n chunks

Chunks a list into n smaller lists.

Use math.ceil() and len() to get the size of each chunk.
Use list() and range() to create a new list of size n.
Use map() to map each element of the new list to a chunk the length of size.
If the original list can't be split evenly, the final chunk will contain the remaining elements.


```py
from math import ceil

def chunk_into_n(lst, n):
  size = ceil(len(lst) / n)
  return list(
    map(lambda x: lst[x * size:x * size + size],
    list(range(n)))
  )

chunk_into_n([1, 2, 3, 4, 5, 6, 7], 4) # [[1, 2], [3, 4], [5, 6], [7]]
```


=======================
Split list into chunks


Chunks a list into smaller lists of a specified size.

Use list() and range() to create a list of the desired size.
Use map() on the list and fill it with splices of the given list.
Finally, return the created list.

```py
from math import ceil

def chunk(lst, size):
  return list(
    map(lambda x: lst[x * size:x * size + size],
      list(range(ceil(len(lst) / size)))))

chunk([1, 2, 3, 4, 5], 2) # [[1, 2], [3, 4], [5]]
```


=======================
Clamp number


Clamps num within the inclusive range specified by the boundary values.

If num falls within the range (a, b), return num.
Otherwise, return the nearest number in the range.

```py
def clamp_number(num, a, b):
  return max(min(num, max(a, b)), min(a, b))

clamp_number(2, 3, 5) # 3
clamp_number(1, -1, -5) # -1
```




=======================
Invert dictionary

Inverts a dictionary with non-unique hashable values.

Create a collections.defaultdict with list as the default value for each key.
Use dictionary.items() in combination with a loop to map the values of the dictionary to keys using dict.append().
Use dict() to convert the collections.defaultdict to a regular dictionary.


```py
from collections import defaultdict

def collect_dictionary(obj):
  inv_obj = defaultdict(list)
  for key, value in obj.items():
    inv_obj[value].append(key)
  return dict(inv_obj)


ages = {
  'Peter': 10,
  'Isabel': 10,
  'Anna': 9,
}

collect_dictionary(ages) # { 10: ['Peter', 'Isabel'], 9: ['Anna'] }
```



=======================
Combine dictionary values

Combines two or more dictionaries, creating a list of values for each key.

Create a new collections.defaultdict with list as the default value for each key and loop over dicts.
Use dict.append() to map the values of the dictionary to keys.
Use dict() to convert the collections.defaultdict to a regular dictionary.

```py
from collections import defaultdict

def combine_values(*dicts):
  res = defaultdict(list)
  for d in dicts:
    for key in d:
      res[key].append(d[key])
  return dict(res)


d1 = {'a': 1, 'b': 'foo', 'c': 400}
d2 = {'a': 3, 'b': 200, 'd': 400}

combine_values(d1, d2) # {'a': [1, 3], 'b': ['foo', 200], 'c': [400], 'd': [400]}
```


=======================
Compact list

Removes falsy values from a list.

Use filter() to filter out falsy values (False, None, 0, and "").


```py
def compact(lst):
  return list(filter(None, lst))

compact([0, 1, False, 2, '', 3, 'a', 's', 34]) # [ 1, 2, 3, 'a', 's', 34 ]
```


=======================
Reverse compose functions


Performs left-to-right function composition.

Use functools.reduce() to perform left-to-right function composition.
The first (leftmost) function can accept one or more arguments; the remaining functions must be unary.

```py
from functools import reduce

def compose_right(*fns):
  return reduce(lambda f, g: lambda *args: g(f(*args)), fns)

add = lambda x, y: x + y
square = lambda x: x * x
add_and_square = compose_right(add, square)
add_and_square(1, 2) # 9
```



=======================
Compose functions


Performs right-to-left function composition.

Use functools.reduce() to perform right-to-left function composition.
The last (rightmost) function can accept one or more arguments; the remaining functions must be unary.


```py
from functools import reduce

def compose(*fns):
  return reduce(lambda f, g: lambda *args: f(g(*args)), fns)


add5 = lambda x: x + 5
multiply = lambda x, y: x * y
multiply_and_add_5 = compose(add5, multiply)
multiply_and_add_5(5, 2) # 15
```




=======================
Count grouped elements

Groups the elements of a list based on the given function and returns the count of elements in each group.

Use collections.defaultdict to initialize a dictionary.
Use map() to map the values of the given list using the given function.
Iterate over the map and increase the element count each time it occurs.

```py
from collections import defaultdict

def count_by(lst, fn = lambda x: x):
  count = defaultdict(int)
  for val in map(fn, lst):
    count[val] += 1
  return dict(count)
from math import floor

count_by([6.1, 4.2, 6.3], floor) # {6: 2, 4: 1}
count_by(['one', 'two', 'three'], len) # {3: 2, 5: 1}
```



=======================
Count occurrences


Counts the occurrences of a value in a list.

Use list.count() to count the number of occurrences of val in lst.

```py
def count_occurrences(lst, val):
  return lst.count(val)


count_occurrences([1, 1, 2, 1, 2, 3], 1) # 3
```




=======================
Partial sum list


Creates a list of partial sums.

Use itertools.accumulate() to create the accumulated sum for each element.
Use list() to convert the result into a list.

```py
from itertools import accumulate

def cumsum(lst):
  return list(accumulate(lst))

cumsum(range(0, 15, 3)) # [0, 3, 9, 18, 30]
```




=======================
Curry function


Curries a function.

Use functools.partial() to return a new partial object which behaves like fn with the given arguments, args, partially applied.

```py
from functools import partial

def curry(fn, *args):
  return partial(fn, *args)


add = lambda x, y: x + y
add10 = curry(add, 10)
add10(20) # 30
```



=======================
Date range

Creates a list of dates between start (inclusive) and end (not inclusive).

Use datetime.timedelta.days to get the days between start and end.
Use int() to convert the result to an integer and range() to iterate over each day.
Use a list comprehension and datetime.timedelta to create a list of datetime.date objects.

```py
from datetime import timedelta, date

def daterange(start, end):
  return [start + timedelta(n) for n in range(int((end - start).days))]
from datetime import date

daterange(date(2020, 10, 1), date(2020, 10, 5))
# [date(2020, 10, 1), date(2020, 10, 2), date(2020, 10, 3), date(2020, 10, 4)]
```



=======================
Days ago


Calculates the date of n days ago from today.

Use datetime.date.today() to get the current day.
Use datetime.timedelta to subtract n days from today's date.

```py
from datetime import timedelta, date

def days_ago(n):
  return date.today() - timedelta(n)

days_ago(5) # date(2020, 10, 23)
```


=======================
Date difference in days

Calculates the day difference between two dates.

Subtract start from end and use datetime.timedelta.days to get the day difference.

```py
def days_diff(start, end):
  return (end - start).days
from datetime import date

days_diff(date(2020, 10, 25), date(2020, 10, 28)) # 3
```




=======================
Days from now

Calculates the date of n days from today.

Use datetime.date.today() to get the current day.
Use datetime.timedelta to add n days from today's date.

```py
from datetime import timedelta, date

def days_from_now(n):
  return date.today() + timedelta(n)


days_from_now(5) # date(2020, 11, 02)
```



=======================
Decapitalize string

Decapitalizes the first letter of a string.

Use list slicing and str.lower() to decapitalize the first letter of the string.
Use str.join() to combine the lowercase first letter with the rest of the characters.
Omit the upper_rest parameter to keep the rest of the string intact, or set it to True to convert to uppercase.

```py
def decapitalize(s, upper_rest = False):
  return ''.join([s[:1].lower(), (s[1:].upper() if upper_rest else s[1:])])


decapitalize('FooBar') # 'fooBar'
decapitalize('FooBar', True) # 'fOOBAR'
```


=======================
Deep flatten list

Deep flattens a list.

Use recursion.
Use isinstance() with collections.abc.Iterable to check if an element is iterable.
If it is iterable, apply deep_flatten() recursively, otherwise return [lst].

```py
from collections.abc import Iterable

def deep_flatten(lst):
  return ([a for i in lst for a in
          deep_flatten(i)] if isinstance(lst, Iterable) else [lst])


deep_flatten([1, [2], [[3], 4], 5]) # [1, 2, 3, 4, 5]
```


=======================
Degrees to radians


Converts an angle from degrees to radians.

Use math.pi and the degrees to radians formula to convert the angle from degrees to radians.

```py
from math import pi

def degrees_to_rads(deg):
  return (deg * pi) / 180.0


degrees_to_rads(180) # ~3.1416
```


=======================
Delayed function execution


Invokes the provided function after ms milliseconds.

Use time.sleep() to delay the execution of fn by ms / 1000 seconds.

```py
from time import sleep

def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)


delay(lambda x: print(x), 1000, 'later') # prints 'later' after one second
```



=======================
Dictionary to list

Converts a dictionary to a list of tuples.

Use dict.items() and list() to get a list of tuples from the given dictionary.

```py
def dict_to_list(d):
  return list(d.items())


d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
dict_to_list(d)
# [('one', 1), ('three', 3), ('five', 5), ('two', 2), ('four', 4)]```
```

=======================
List difference based on function

Returns the difference between two lists, after applying the provided function to each list element of both.

Create a set, using map() to apply fn to each element in b.
Use a list comprehension in combination with fn on a to only keep values not contained in the previously created set, _b.


```py
def difference_by(a, b, fn):
  _b = set(map(fn, b))
  return [item for item in a if fn(item) not in _b]
from math import floor

difference_by([2.1, 1.2], [2.3, 3.4], floor) # [1.2]
difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x'])
# [ { x: 2 } ]
```


=======================
List difference


Calculates the difference between two iterables, without filtering duplicate values.

Create a set from b.
Use a list comprehension on a to only keep values not contained in the previously created set, _b.

```py
def difference(a, b):
  _b = set(b)
  return [item for item in a if item not in _b]

difference([1, 2, 3], [1, 2, 4]) # [3]
```



=======================
Digitize number


Converts a number to a list of digits.

Use map() combined with int on the string representation of n and return a list from the result.


```py
def digitize(n):
  return list(map(int, str(n)))

digitize(123) # [1, 2, 3]
```


=======================
Drop list elements from the right

Returns a list with n elements removed from the right.

Use slice notation to remove the specified number of elements from the right.

Omit the last argument, n, to use a default value of 1.


```py

def drop_right(a, n = 1):
  return a[:-n]

drop_right([1, 2, 3]) # [1, 2]
drop_right([1, 2, 3], 2) # [1]
drop_right([1, 2, 3], 42) # []
```


=======================
Drop list elements from the left


Returns a list with n elements removed from the left.

Use slice notation to remove the specified number of elements from the left.
Omit the last argument, n, to use a default value of 1.


```py
def drop(a, n = 1):
  return a[n:]

drop([1, 2, 3]) # [2, 3]
drop([1, 2, 3], 2) # [3]
drop([1, 2, 3], 42) # []
```




=======================
Every nth element in list

Returns every nth element in a list.

Use slice notation to create a new list that contains every nth element of the given list.

```py
def every_nth(lst, nth):
  return lst[nth - 1::nth]

every_nth([1, 2, 3, 4, 5, 6], 2) # [ 2, 4, 6 ]
```


=======================
Test if every list element is truthy

Checks if the provided function returns True for every element in the list.

Use all() in combination with map() and fn to check if fn returns True for all elements in the list.

```py
def every(lst, fn = lambda x: x):
  return all(map(fn, lst))

every([4, 2, 3], lambda x: x > 1) # True
every([1, 2, 3]) # True
```


=======================
Factorial

Calculates the factorial of a number.

Use recursion.
If num is less than or equal to 1, return 1.
Otherwise, return the product of num and the factorial of num - 1.
Throws an exception if num is a negative or a floating point number.

```py
def factorial(num):
  if not ((num >= 0) and (num % 1 == 0)):
    raise Exception("Number can't be floating point or negative.")
  return 1 if num == 0 else num * factorial(num - 1)

factorial(6) # 720
```


=======================
Fahrenheit to Celsius


Converts Fahrenheit to Celsius.

Follow the conversion formula C = (F - 32) * 5 / 9.

```py
def fahrenheit_to_celsius(degrees):
  return ((degrees - 32) * 5 / 9)

fahrenheit_to_celsius(77) # 25.0
```


=======================
Fibonacci

Generates a list, containing the Fibonacci sequence, up until the nth term.

Starting with 0 and 1, use list.append() to add the sum of the last two numbers of the list to the end of the list, until the length of the list reaches n.
If n is less or equal to 0, return a list containing 0.

```py
def fibonacci(n):
  if n <= 0:
    return [0]
  sequence = [0, 1]
  while len(sequence) <= n:
    next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
    sequence.append(next_value)
  return sequence

fibonacci(7) # [0, 1, 1, 2, 3, 5, 8, 13]
```


=======================
Filter non-unique list values

Creates a list with the non-unique values filtered out.

Use collections.Counter to get the count of each value in the list.
Use a list comprehension to create a list containing only the unique values.
from collections import Counter

```py
def filter_non_unique(lst):
  return [item for item, count in Counter(lst).items() if count == 1]

filter_non_unique([1, 2, 2, 3, 4, 4, 5]) # [1, 3, 5]
```



=======================
Filter unique list values


Creates a list with the unique values filtered out.

Use collections.Counter to get the count of each value in the list.
Use a list comprehension to create a list containing only the non-unique values.
from collections import Counter

```py
def filter_unique(lst):
  return [item for item, count in Counter(lst).items() if count > 1]

filter_unique([1, 2, 2, 3, 4, 4, 5]) # [2, 4]
```


=======================
Find all matching indexes

Finds the indexes of all elements in the given list that satisfy the provided testing function.

Use enumerate() and a list comprehension to return the indexes of the all element in lst for which fn returns True.

```py
def find_index_of_all(lst, fn):
  return [i for i, x in enumerate(lst) if fn(x)]

find_index_of_all([1, 2, 3, 4], lambda n: n % 2 == 1) # [0, 2]
```



=======================
Find matching index


Finds the index of the first element in the given list that satisfies the provided testing function.

Use a list comprehension, enumerate() and next() to return the index of the first element in lst for which fn returns True.

```py
def find_index(lst, fn):
  return next(i for i, x in enumerate(lst) if fn(x))

find_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 0
```


=======================
Find key of value

Finds the first key in the provided dictionary that has the given value.

Use dictionary.items() and next() to return the first key that has a value equal to val.

```py
def find_key(dict, val):
  return next(key for key, value in dict.items() if value == val)
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}

find_key(ages, 11) # 'Isabel'
```


=======================
Find keys with value

Finds all keys in the provided dictionary that have the given value.

Use dictionary.items(), a generator and list() to return all keys that have a value equal to val.

```py
def find_keys(dict, val):
  return list(key for key, value in dict.items() if value == val)
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 10,
}

find_keys(ages, 10) # [ 'Peter', 'Anna' ]
```



=======================
Find last matching index

Finds the index of the last element in the given list that satisfies the provided testing function.

Use a list comprehension, enumerate() and next() to return the index of the last element in lst for which fn returns True.

```py
def find_last_index(lst, fn):
  return len(lst) - 1 - next(i for i, x in enumerate(lst[::-1]) if fn(x))

```



=======================
Find last matching value

Finds the value of the last element in the given list that satisfies the provided testing function.

Use a list comprehension and next() to return the last element in lst for which fn returns True.

```py
def find_last(lst, fn):
  return next(x for x in lst[::-1] if fn(x))

find_last([1, 2, 3, 4], lambda n: n % 2 == 1) # 3
```



=======================
Find parity outliers

Finds the items that are parity outliers in a given list.

Use collections.Counter with a list comprehension to count even and odd values in the list.
Use collections.Counter.most_common() to get the most common parity.
Use a list comprehension to find all elements that do not match the most common parity.
from collections import Counter

```py
def find_parity_outliers(nums):
  return [
    x for x in nums
    if x % 2 != Counter([n % 2 for n in nums]).most_common()[0][0]
  ]

find_parity_outliers([1, 2, 3, 4, 6]) # [1, 3]
```



=======================
Find matching value

Finds the value of the first element in the given list that satisfies the provided testing function.

Use a list comprehension and next() to return the first element in lst for which fn returns True.

```py
def find(lst, fn):
  return next(x for x in lst if fn(x))

find([1, 2, 3, 4], lambda n: n % 2 == 1) # 1
```


=======================
Flatten list

Flattens a list of lists once.

Use a list comprehension to extract each value from sub-lists in order.

```py
def flatten(lst):
  return [x for y in lst for x in y]

flatten([[1, 2, 3, 4], [5, 6, 7, 8]]) # [1, 2, 3, 4, 5, 6, 7, 8]
```



=======================
Execute function for each list element in reverse

Executes the provided function once for each list element, starting from the list's last element.

Use a for loop in combination with slice notation to execute fn for each element in itr, starting from the last one.

```py
def for_each_right(itr, fn):
  for el in itr[::-1]:
    fn(el)

for_each_right([1, 2, 3], print) # 3 2 1
```


=======================
Execute function for each list element


Executes the provided function once for each list element.

Use a for loop to execute fn for each element in itr.

```py
def for_each(itr, fn):
  for el in itr:
    fn(el)

for_each([1, 2, 3], print) # 1 2 3
```

=======================
Value frequencies

Creates a dictionary with the unique values of a list as keys and their frequencies as the values.

Use collections.defaultdict to store the frequencies of each unique element.
Use dict() to return a dictionary with the unique elements of the list as keys and their frequencies as the values.
from collections import defaultdict

```py
def frequencies(lst):
  freq = defaultdict(int)
  for val in lst:
    freq[val] += 1
  return dict(freq)

frequencies(['a', 'b', 'a', 'c', 'a', 'a', 'b']) # { 'a': 4, 'b': 2, 'c': 1 }
```


=======================
Date from ISO format


Converts a date from its ISO-8601 representation.

Use datetime.datetime.fromisoformat() to convert the given ISO-8601 date to a datetime.datetime object.
from datetime import datetime

```py
def from_iso_date(d):
  return datetime.fromisoformat(d)

from_iso_date('2020-10-28T12:30:59.000000') # 2020-10-28 12:30:59
```

=======================
Greatest common divisor

Calculates the greatest common divisor of a list of numbers.

Use functools.reduce() and math.gcd() over the given list.
from functools import reduce
from math import gcd as _gcd

```py
def gcd(numbers):
  return reduce(_gcd, numbers)

gcd([8, 36, 28]) # 4
```


=======================
Geometric progression


Initializes a list containing the numbers in the specified range where start and end are inclusive and the ratio between two terms is step.

Use range(), math.log() and math.floor() and a list comprehension to create a list of the appropriate length, applying the step for each element.
Returns an error if step equals 1.
Omit the second argument, start, to use a default value of 1.
Omit the third argument, step, to use a default value of 2.
from math import floor, log

```py
def geometric_progression(end, start=1, step=2):
  return [start * step ** i for i in range(floor(log(end / start)
          / log(step)) + 1)]

geometric_progression(256) # [1, 2, 4, 8, 16, 32, 64, 128, 256]
geometric_progression(256, 3) # [3, 6, 12, 24, 48, 96, 192]
geometric_progression(256, 1, 4) # [1, 4, 16, 64, 256]
```


=======================
Get nested value

Retrieves the value of the nested key indicated by the given selector list from a dictionary or list.

Use functools.reduce() to iterate over the selectors list.
Apply operator.getitem() for each key in selectors, retrieving the value to be used as the iteratee for the next iteration.
from functools import reduce
from operator import getitem

```py
def get(d, selectors):
  return reduce(getitem, selectors, d)
users = {
  'freddy': {
    'name': {
      'first': 'fred',
      'last': 'smith'
    },
    'postIds': [1, 2, 3]
  }
}

get(users, ['freddy', 'name', 'last']) # 'smith'
get(users, ['freddy', 'postIds', 1]) # 2
```



=======================
Group list elements


Groups the elements of a list based on the given function.

Use collections.defaultdict to initialize a dictionary.
Use fn in combination with a for loop and dict.append() to populate the dictionary.
Use dict() to convert it to a regular dictionary.
from collections import defaultdict

```py
def group_by(lst, fn):
  d = defaultdict(list)
  for el in lst:
    d[fn(el)].append(el)
  return dict(d)
from math import floor

group_by([6.1, 4.2, 6.3], floor) # {4: [4.2], 6: [6.1, 6.3]}
group_by(['one', 'two', 'three'], len) # {3: ['one', 'two'], 5: ['three']}
```



=======================
Hamming distance

Calculates the Hamming distance between two values.

Use the XOR operator (^) to find the bit difference between the two numbers.
Use bin() to convert the result to a binary string.
Convert the string to a list and use count() of str class to count and return the number of 1s in it.

```py
def hamming_distance(a, b):
  return bin(a ^ b).count('1')

hamming_distance(2, 3) # 1
```



=======================
Check for duplicates in list

Checks if there are duplicate values in a flat list.

Use set() on the given list to remove duplicates, compare its length with the length of the list.

```py
def has_duplicates(lst):
  return len(lst) != len(set(lst))

x = [1, 2, 3, 4, 5, 5]
y = [1, 2, 3, 4, 5]

has_duplicates(x) # True
has_duplicates(y) # False
```


=======================
Check lists have same contents

Checks if two lists contain the same elements regardless of order.

Use set() on the combination of both lists to find the unique values.
Iterate over them with a for loop comparing the count() of each unique value in each list.
Return False if the counts do not match for any element, True otherwise.

```py
def have_same_contents(a, b):
  for v in set(a + b):
    if a.count(v) != b.count(v):
      return False
  return True

have_same_contents([1, 2, 4], [2, 4, 1]) # True
```



=======================
List head

Returns the head of a list.

Use lst[0] to return the first element of the passed list.

```py
def head(lst):
  return lst[0]

head([1, 2, 3]) # 1
```



=======================
Hex to RGB

Converts a hexadecimal color code to a tuple of integers corresponding to its RGB components.

Use a list comprehension in combination with int() and list slice notation to get the RGB components from the hexadecimal string.
Use tuple() to convert the resulting list to a tuple.

```py
def hex_to_rgb(hex):
  return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

hex_to_rgb('FFA501') # (255, 165, 1)
```


=======================
Number in range


Checks if the given number falls within the given range.

Use arithmetic comparison to check if the given number is in the specified range.
If the second parameter, end, is not specified, the range is considered to be from 0 to start.


```py
def in_range(n, start, end = 0):
  return start <= n <= end if end >= start else end <= n <= start

in_range(3, 2, 5) # True
in_range(3, 4) # True
in_range(2, 3, 5) # False
in_range(3, 2) # False
```

=======================
List includes all values


Checks if all the elements in values are included in lst.

Check if every value in values is contained in lst using a for loop.
Return False if any one value is not found, True otherwise.

```py
def includes_all(lst, values):
  for v in values:
    if v not in lst:
      return False
  return True

includes_all([1, 2, 3, 4], [1, 4]) # True
includes_all([1, 2, 3, 4], [1, 5]) # False
```



=======================
List includes any values

Checks if any element in values is included in lst.

Check if any value in values is contained in lst using a for loop.
Return True if any one value is found, False otherwise.

```py
def includes_any(lst, values):
  for v in values:
    if v in lst:
      return True
  return False

includes_any([1, 2, 3, 4], [2, 9]) # True
includes_any([1, 2, 3, 4], [8, 9]) # False
```



=======================
All indexes of value


eturns a list of indexes of all the occurrences of an element in a list.

Use enumerate() and a list comprehension to check each element for equality with value and adding i to the result.

```py
def index_of_all(lst, value):
  return [i for i, x in enumerate(lst) if x == value]

index_of_all([1, 2, 1, 4, 5, 1], 1) # [0, 2, 5]
index_of_all([1, 2, 3, 4], 6) # []
```


=======================
List without last element

Returns all the elements of a list except the last one.

Use lst[:-1] to return all but the last element of the list.

```py
def initial(lst):
  return lst[:-1]

initial([1, 2, 3]) # [1, 2]
```


=======================
Initialize 2D list

Initializes a 2D list of given width and height and value.

Use a list comprehension and range() to generate h rows where each is a list with length h, initialized with val.
Omit the last argument, val, to set the default value to None.


```py
def initialize_2d_list(w, h, val = None):
  return [[val for x in range(w)] for y in range(h)]

initialize_2d_list(2, 2, 0) # [[0, 0], [0, 0]]
```


=======================
Initialize list with range

Initializes a list containing the numbers in the specified range where start and end are inclusive with their common difference step.

Use list() and range() to generate a list of the appropriate length, filled with the desired values in the given range.
Omit start to use the default value of 0.
Omit step to use the default value of 1.


```py
def initialize_list_with_range(end, start = 0, step = 1):
  return list(range(start, end + 1, step))

initialize_list_with_range(5) # [0, 1, 2, 3, 4, 5]
initialize_list_with_range(7, 3) # [3, 4, 5, 6, 7]
initialize_list_with_range(9, 0, 2) # [0, 2, 4, 6, 8]
```


=======================
Initialize list with values

Initializes and fills a list with the specified value.

Use a list comprehension and range() to generate a list of length equal to n, filled with the desired values.
Omit val to use the default value of 0.


```py
def initialize_list_with_values(n, val = 0):
  return [val for x in range(n)]

initialize_list_with_values(5, 2) # [2, 2, 2, 2, 2]
```


=======================
List intersection based on function

Returns a list of elements that exist in both lists, after applying the provided function to each list element of both.

Create a set, using map() to apply fn to each element in b.
Use a list comprehension in combination with fn on a to only keep values contained in both lists.

```py
def intersection_by(a, b, fn):
  _b = set(map(fn, b))
  return [item for item in a if fn(item) in _b]
from math import floor

intersection_by([2.1, 1.2], [2.3, 3.4], floor) # [2.1]
```



=======================
List intersection

Returns a list of elements that exist in both lists.

Create a set from a and b.
Use the built-in set operator & to only keep values contained in both sets, then transform the set back into a list.

```py
def intersection(a, b):
  _a, _b = set(a), set(b)
  return list(_a & _b)

intersection([1, 2, 3], [4, 3, 2]) # [2, 3]
```


=======================
Invert dictionary


Inverts a dictionary with unique hashable values.

Use dictionary.items() in combination with a list comprehension to create a new dictionary with the values and keys inverted.


```py
def invert_dictionary(obj):
  return { value: key for key, value in obj.items() }
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}

invert_dictionary(ages) # { 10: 'Peter', 11: 'Isabel', 9: 'Anna' }
```

=======================
String is anagram

Checks if a string is an anagram of another string (case-insensitive, ignores spaces, punctuation and special characters).

Use str.isalnum() to filter out non-alphanumeric characters, str.lower() to transform each character to lowercase.
Use collections.Counter to count the resulting characters for each string and compare the results.
from collections import Counter


```py
def is_anagram(s1, s2):
  return Counter(
    c.lower() for c in s1 if c.isalnum()
  ) == Counter(
    c.lower() for c in s2 if c.isalnum()
  )

is_anagram('#anagram', 'Nag a ram!')  # True
```



=======================
List is contained in other list


Checks if the elements of the first list are contained in the second one regardless of order.

Use count() to check if any value in a has more occurrences than it has in b.
Return False if any such value is found, True otherwise.


```py
def is_contained_in(a, b):
  for v in set(a):
    if a.count(v) > b.count(v):
      return False
  return True

is_contained_in([1, 4], [2, 4, 1]) # True
```


=======================
Number is divisible

Checks if the first numeric argument is divisible by the second one.

Use the modulo operator (%) to check if the remainder is equal to 0.



```py
def is_divisible(dividend, divisor):
  return dividend % divisor == 0

is_divisible(6, 3) # True
```



=======================
Collection is empty

Checks if the a value is an empty sequence or collection.

Use not to test the truth value of the provided sequence or collection.


```py
def is_empty(val):
  return not val

is_empty([]) # True
is_empty({}) # True
is_empty('') # True
is_empty(set()) # True
is_empty(range(0)) # True
is_empty([1, 2]) # False
is_empty({ 'a': 1, 'b': 2 }) # False
is_empty('text') # False
is_empty(set([1, 2])) # False
is_empty(range(2)) # False
```



=======================
Number is even


Checks if the given number is even.

Check whether a number is odd or even using the modulo (%) operator.
Return True if the number is even, False if the number is odd.

```py
def is_even(num):
  return num % 2 == 0

is_even(3) # False
```

=======================
Number is odd


Checks if the given number is odd.

Checks whether a number is even or odd using the modulo (%) operator.
Returns True if the number is odd, False if the number is even.

```py
def is_odd(num):
  return num % 2 != 0

is_odd(3) # True
```



=======================
Number is prime


Checks if the provided integer is a prime number.

Return False if the number is 0, 1, a negative number or a multiple of 2.
Use all() and range() to check numbers from 3 to the square root of the given number.
Return True if none divides the given number, False otherwise.
from math import sqrt

```py
def is_prime(n):
  if n <= 1 or (n % 2 == 0 and n > 2):
    return False
  return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))
is_prime(11) # True
```


=======================
Date is weekday


Checks if the given date is a weekday.

Use datetime.datetime.weekday() to get the day of the week as an integer.
Check if the day of the week is less than or equal to 4.
Omit the second argument, d, to use a default value of datetime.today().
from datetime import datetime

```py
def is_weekday(d = datetime.today()):
  return d.weekday() <= 4

from datetime import date

is_weekday(date(2020, 10, 25)) # False
is_weekday(date(2020, 10, 28)) # True
```




=======================
Date is weekend

Checks if the given date is a weekend.

Use datetime.datetime.weekday() to get the day of the week as an integer.
Check if the day of the week is greater than 4.
Omit the second argument, d, to use a default value of datetime.today().
from datetime import datetime

```py
def is_weekend(d = datetime.today()):
  return d.weekday() > 4
from datetime import date

is_weekend(date(2020, 10, 25)) # True
is_weekend(date(2020, 10, 28)) # False
```



=======================
Kebabcase string


Converts a string to kebab case.

- Use `re.sub()` to replace any `-` or `_` with a space, using the regexp `r"(_|-)+"`.
- Use `re.sub()` to match all words in the string, `str.lower()` to lowercase them.
- Finally, use `str.join()` to combine all word using `-` as the separator.

```py
from re import sub

def kebab(s):
  return '-'.join(
    sub(r"(\s|_|-)+"," ",
    sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
    lambda mo: ' ' + mo.group(0).lower(), s)).split())
```

```py
kebab('camelCase') # 'camel-case'
kebab('some text') # 'some-text'
kebab('some-mixed_string With spaces_underscores-and-hyphens')
# 'some-mixed-string-with-spaces-underscores-and-hyphens'
kebab('AllThe-small Things') # 'all-the-small-things'
```


=======================
Key in dictionary


Checks if the given key exists in a dictionary.

- Use the `in` operator to check if `d` contains `key`.

```py
def key_in_dict(d, key):
  return (key in d)
```

```py
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
key_in_dict(d, 'three') # True
```



=======================
Key of max value

Finds the key of the maximum value in a dictionary.

- Use `max()` with the `key` parameter set to `dict.get()` to find and return the key of the maximum value in the given dictionary.

```py
def key_of_max(d):
  return max(d, key = d.get)
```

```py
key_of_max({'a':4, 'b':0, 'c':13}) # c
```



=======================
Key of min value

Finds the key of the minimum value in a dictionary.

- Use `min()` with the `key` parameter set to `dict.get()` to find and return the key of the minimum value in the given dictionary.

```py
def key_of_min(d):
  return min(d, key = d.get)
```

```py
key_of_min({'a':4, 'b':0, 'c':13}) # b
```


=======================
Dictionary keys

Creates a flat list of all the keys in a flat dictionary.

- Use `dict.keys()` to return the keys in the given dictionary.
- Return a `list()` of the previous result.

```py
def keys_only(flat_dict):
  return list(flat_dict.keys())
```

```py
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
keys_only(ages) # ['Peter', 'Isabel', 'Anna']
```

=======================
Km to miles

Converts kilometers to miles.

- Follows the conversion formula `mi = km * 0.621371`.

```py
def km_to_miles(km):
  return km * 0.621371
```

```py
km_to_miles(8.1) # 5.0331051
```

=======================
Last list element

Returns the last element in a list.

- Use `lst[-1]` to return the last element of the passed list.

```py
def last(lst):
  return lst[-1]
```

```py
last([1, 2, 3]) # 3
```

=======================
Least common multiple

Returns the least common multiple of a list of numbers.

- Use `functools.reduce()`, `math.gcd()` and `lcm(x, y) = x * y / gcd(x, y)` over the given list.

```py
from functools import reduce
from math import gcd

def lcm(numbers):
  return reduce((lambda x, y: int(x * y / gcd(x, y))), numbers)
```

```py
lcm([12, 7]) # 84
lcm([1, 3, 4, 5]) # 60
```



=======================
Longest item

Takes any number of iterable objects or objects with a length property and returns the longest one.

- Use `max()` with `len()` as the `key` to return the item with the greatest length.
- If multiple items have the same length, the first one will be returned.

```py
def longest_item(*args):
  return max(args, key = len)
```

```py
longest_item('this', 'is', 'a', 'testcase') # 'testcase'
longest_item([1, 2, 3], [1, 2], [1, 2, 3, 4, 5]) # [1, 2, 3, 4, 5]
longest_item([1, 2, 3], 'foobar') # 'foobar'
```



=======================
Map list to dictionary

Maps the values of a list to a dictionary using a function, where the key-value pairs consist of the original value as the key and the result of the function as the value.

- Use `map()` to apply `fn` to each value of the list.
- Use `zip()` to pair original values to the values produced by `fn`.
- Use `dict()` to return an appropriate dictionary.

```py
def map_dictionary(itr, fn):
  return dict(zip(itr, map(fn, itr)))
```

```py
map_dictionary([1, 2, 3], lambda x: x * x) # { 1: 1, 2: 4, 3: 9 }
```


=======================
Map dictionary values

Creates a dictionary with the same keys as the provided dictionary and values generated by running the provided function for each value.

- Use `dict.items()` to iterate over the dictionary, assigning the values produced by `fn` to each key of a new dictionary.

```py
def map_values(obj, fn):
  return dict((k, fn(v)) for k, v in obj.items())
```

```py
users = {
  'fred': { 'user': 'fred', 'age': 40 },
  'pebbles': { 'user': 'pebbles', 'age': 1 }
}
map_values(users, lambda u : u['age']) # {'fred': 40, 'pebbles': 1}
```


=======================
Max list value based on function

Returns the maximum value of a list, after mapping each element to a value using the provided function.

- Use `map()` with `fn` to map each element to a value using the provided function.
- Use `max()` to return the maximum value.

```py
def max_by(lst, fn):
  return max(map(fn, lst))
```

```py
max_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 8
```


=======================
Index of max element

Returns the index of the element with the maximum value in a list.

- Use `max()` and `list.index()` to get the maximum value in the list and return its index.

```py
def max_element_index(arr):
  return arr.index(max(arr))
```

```py
max_element_index([5, 8, 9, 7, 10, 3, 0]) # 4
```


=======================
N max elements

Returns the `n` maximum elements from the provided list.

- Use `sorted()` to sort the list.
- Use slice notation to get the specified number of elements.
- Omit the second argument, `n`, to get a one-element list.
- If `n` is greater than or equal to the provided list's length, then return the original list (sorted in descending order).

```py
def max_n(lst, n = 1):
  return sorted(lst, reverse = True)[:n]
```

```py
max_n([1, 2, 3]) # [3]
max_n([1, 2, 3], 2) # [3, 2]
```


=======================
Median

Finds the median of a list of numbers.

- Sort the numbers of the list using `list.sort()`.
- Find the median, which is either the middle element of the list if the list length is odd or the average of the two middle elements if the list length is even.
- [`statistics.median()`](https://docs.python.org/3/library/statistics.html#statistics.median) provides similar functionality to this snippet.

```py
def median(list):
  list.sort()
  list_length = len(list)
  if list_length % 2 == 0:
    return (list[int(list_length / 2) - 1] + list[int(list_length / 2)]) / 2
  return float(list[int(list_length / 2)])
```

```py
median([1, 2, 3]) # 2.0
median([1, 2, 3, 4]) # 2.5
```

=======================
Merge dictionaries

Merges two or more dictionaries.

- Create a new `dict` and loop over `dicts`, using `dictionary.update()` to add the key-value pairs from each one to the result.

```py
def merge_dictionaries(*dicts):
  res = dict()
  for d in dicts:
    res.update(d)
  return res
```

```py
ages_one = {
  'Peter': 10,
  'Isabel': 11,
}
ages_two = {
  'Anna': 9
}
merge_dictionaries(ages_one, ages_two)
# { 'Peter': 10, 'Isabel': 11, 'Anna': 9 }
```

=======================
Merge lists

Merges two or more lists into a list of lists, combining elements from each of the input lists based on their positions.

- Use `max()` combined with a list comprehension to get the length of the longest list in the arguments.
- Use `range()` in combination with the `max_length` variable to loop as many times as there are elements in the longest list.
- If a list is shorter than `max_length`, use `fill_value` for the remaining items (defaults to `None`).
- [`zip()`](https://docs.python.org/3/library/functions.html#zip) and [`itertools.zip_longest()`](https://docs.python.org/3/library/itertools.html#itertools.zip_longest) provide similar functionality to this snippet.

```py
def merge(*args, fill_value = None):
  max_length = max([len(lst) for lst in args])
  result = []
  for i in range(max_length):
    result.append([
      args[k][i] if i < len(args[k]) else fill_value for k in range(len(args))
    ])
  return result
```

```py
merge(['a', 'b'], [1, 2], [True, False]) # [['a', 1, True], ['b', 2, False]]
merge(['a'], [1, 2], [True, False]) # [['a', 1, True], [None, 2, False]]
merge(['a'], [1, 2], [True, False], fill_value = '_')
# [['a', 1, True], ['_', 2, False]]
```


=======================
Miles to km

Converts miles to kilometers.

- Follows the conversion formula `km = mi * 1.609344`.

```py
def miles_to_km(miles):
  return miles * 1.609344

miles_to_km(5.03) # 8.09500032
```


=======================
Min list value based on function

Returns the minimum value of a list, after mapping each element to a value using the provided function.

- Use `map()` with `fn` to map each element to a value using the provided function.
- Use `min()` to return the minimum value.

```py
def min_by(lst, fn):
  return min(map(fn, lst))
```

```py
min_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 2
```

=======================
Index of min element

Returns the index of the element with the minimum value in a list.

- Use `min()` and `list.index()` to obtain the minimum value in the list and then return its index.

```py
def min_element_index(arr):
  return arr.index(min(arr))
```

```py
min_element_index([3, 5, 2, 6, 10, 7, 9]) # 2
```


=======================
N min elements

Returns the `n` minimum elements from the provided list.

- Use `sorted()` to sort the list.
- Use slice notation to get the specified number of elements.
- Omit the second argument, `n`, to get a one-element list.
- If `n` is greater than or equal to the provided list's length, then return the original list (sorted in ascending order).

```py
def min_n(lst, n = 1):
  return sorted(lst, reverse = False)[:n]
```

```py
min_n([1, 2, 3]) # [1]
min_n([1, 2, 3], 2) # [1, 2]
```

=======================
Date difference in months

Calculates the month difference between two dates.

- Subtract `start` from `end` and use `datetime.timedelta.days` to get the day difference.
- Divide by `30` and use `math.ceil()` to get the difference in months (rounded up).

```py
from math import ceil

def months_diff(start, end):
  return ceil((end - start).days / 30)
```

```py
from datetime import date

months_diff(date(2020, 10, 28), date(2020, 11, 25)) # 1
```


=======================
Most frequent element

Returns the most frequent element in a list.

- Use `set()` to get the unique values in `lst`.
- Use `max()` to find the element that has the most appearances.

```py
def most_frequent(lst):
  return max(set(lst), key = lst.count)
```

```py
most_frequent([1, 2, 1, 2, 3, 2, 1, 4, 2]) #2
```

=======================
Repeat string

Generates a string with the given string value repeated `n` number of times.

- Repeat the string `n` times, using the `*` operator.

```py
def n_times_string(s, n):
  return (s * n)
```

```py
n_times_string('py', 4) #'pypypypy'
```

=======================
Test if every list element is falsy

Checks if the provided function returns `True` for at least one element in the list.

- Use `all()` and `fn` to check if `fn` returns `False` for all the elements in the list.

```py
def none(lst, fn = lambda x: x):
  return all(not fn(x) for x in lst)
```

```py
none([0, 1, 2, 0], lambda x: x >= 2 ) # False
none([0, 0, 0]) # True
```

=======================
Map number to range

Maps a number from one range to another range.

- Return `num` mapped between `outMin`-`outMax` from `inMin`-`inMax`.

```py
def num_to_range(num, inMin, inMax, outMin, outMax):
  return outMin + (float(num - inMin) / float(inMax - inMin) * (outMax
                  - outMin))
```

```py
num_to_range(5, 0, 10, 0, 100) # 50.0
```


=======================
Offset list elements


Moves the specified amount of elements to the end of the list.

- Use slice notation to get the two slices of the list and combine them before returning.

```py
def offset(lst, offset):
  return lst[offset:] + lst[:offset]
```

```py
offset([1, 2, 3, 4, 5], 2) # [3, 4, 5, 1, 2]
offset([1, 2, 3, 4, 5], -2) # [4, 5, 1, 2, 3]
```

=======================
Pad number


Pads a given number to the specified length.

- Use `str.zfill()` to pad the number to the specified length, after converting it to a string.

```py
def pad_number(n, l):
  return str(n).zfill(l)
```

```py
pad_number(1234, 6); # '001234'
```


=======================
Pad string

Pads a string on both sides with the specified character, if it's shorter than the specified length.

- Use `str.ljust()` and `str.rjust()` to pad both sides of the given string.
- Omit the third argument, `char`, to use the whitespace character as the default padding character.

```py
from math import floor

def pad(s, length, char = ' '):
  return s.rjust(floor((len(s) + length)/2), char).ljust(length, char)
```

```py
pad('cat', 8) # '  cat   '
pad('42', 6, '0') # '004200'
pad('foobar', 3) # 'foobar'
```


=======================
Palindrome

Checks if the given string is a palindrome.

- Use `str.lower()` and `re.sub()` to convert to lowercase and remove non-alphanumeric characters from the given string.
- Then, compare the new string with its reverse, using slice notation.

```py
from re import sub

def palindrome(s):
  s = sub('[\W_]', '', s.lower())
  return s == s[::-1]
```

```py
palindrome('taco cat') # True
```


=======================
Pluck values from list of dictionaries

Converts a list of dictionaries into a list of values corresponding to the specified `key`.

- Use a list comprehension and `dict.get()` to get the value of `key` for each dictionary in `lst`.

```py
def pluck(lst, key):
  return [x.get(key) for x in lst]
```

```py
simpsons = [
  { 'name': 'lisa', 'age': 8 },
  { 'name': 'homer', 'age': 36 },
  { 'name': 'marge', 'age': 34 },
  { 'name': 'bart', 'age': 10 }
]
pluck(simpsons, 'age') # [8, 36, 34, 10]
```


=======================
Powerset

Returns the powerset of a given iterable.

- Use `list()` to convert the given value to a list.
- Use `range()` and `itertools.combinations()` to create a generator that returns all subsets.
- Use `itertools.chain.from_iterable()` and `list()` to consume the generator and return a list.

```py
from itertools import chain, combinations

def powerset(iterable):
  s = list(iterable)
  return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
```

```py
powerset([1, 2]) # [(), (1,), (2,), (1, 2)]
```


=======================
Radians to degrees

Converts an angle from radians to degrees.

- Use `math.pi` and the radian to degree formula to convert the angle from radians to degrees.

```py
from math import pi

def rads_to_degrees(rad):
  return (rad * 180.0) / pi
```

```py
from math import pi

rads_to_degrees(pi / 2) # 90.0
```

=======================
Reverse number

Reverses a number.

- Use `str()` to convert the number to a string, slice notation to reverse it and `str.replace()` to remove the sign.
- Use `float()` to convert the result to a number and `math.copysign()` to copy the original sign.

```py
from math import copysign

def reverse_number(n):
  return copysign(float(str(n)[::-1].replace('-', '')), n)
```

```py
reverse_number(981) # 189
reverse_number(-500) # -5
reverse_number(73.6) # 6.37
reverse_number(-5.23) # -32.5
```


=======================
Reverse list

Reverses a list or a string.

- Use slice notation to reverse the list or string.

```py
def reverse(itr):
  return itr[::-1]
```

```py
reverse([1, 2, 3]) # [3, 2, 1]
reverse('snippet') # 'teppins'
```

=======================
RGB to hex

Converts the values of RGB components to a hexadecimal color code.

- Create a placeholder for a zero-padded hexadecimal value using `'{:02X}'` and copy it three times.
- Use `str.format()` on the resulting string to replace the placeholders with the given values.

```py
def rgb_to_hex(r, g, b):
  return ('{:02X}' * 3).format(r, g, b)
```

```py
rgb_to_hex(255, 165, 1) # 'FFA501'
```

=======================
Rotate list elements

Moves the specified amount of elements to the start of the list.

- Use slice notation to get the two slices of the list and combine them before returning.

```py
def roll(lst, offset):
  return lst[-offset:] + lst[:-offset]
```

```py
roll([1, 2, 3, 4, 5], 2) # [4, 5, 1, 2, 3]
roll([1, 2, 3, 4, 5], -2) # [3, 4, 5, 1, 2]
```


=======================
Random element in list

Returns a random element from a list.

- Use `random.choice()` to get a random element from `lst`.

```py
from random import choice

def sample(lst):
  return choice(lst)
```

```py
sample([3, 7, 9, 11]) # 9
```



=======================
Shuffle list

Randomizes the order of the values of an list, returning a new list.

- Uses the [Fisher-Yates algorithm](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle) to reorder the elements of the list.
- [`random.shuffle`](https://docs.python.org/3/library/random.html#random.shuffle) provides similar functionality to this snippet.

```py
from copy import deepcopy
from random import randint

def shuffle(lst):
  temp_lst = deepcopy(lst)
  m = len(temp_lst)
  while (m):
    m -= 1
    i = randint(0, m)
    temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
  return temp_lst
```

```py
foo = [1, 2, 3]
shuffle(foo) # [2, 3, 1], foo = [1, 2, 3]
```

=======================
List similarity

Returns a list of elements that exist in both lists.

- Use a list comprehension on `a` to only keep values contained in both lists.

```py
def similarity(a, b):
  return [item for item in a if item in b]
```

```py
similarity([1, 2, 3], [1, 2, 4]) # [1, 2]
```

=======================
String to slug

Converts a string to a URL-friendly slug.

- Use `str.lower()` and `str.strip()` to normalize the input string.
- Use `re.sub()` to to replace spaces, dashes and underscores with `-` and remove special characters.

```py
import re

def slugify(s):
  s = s.lower().strip()
  s = re.sub(r'[^\w\s-]', '', s)
  s = re.sub(r'[\s_-]+', '-', s)
  s = re.sub(r'^-+|-+$', '', s)
  return s
```

```py
slugify('Hello World!') # 'hello-world'
```


=======================
Snakecase string

Converts a string to snake case.

- Use `re.sub()` to match all words in the string, `str.lower()` to lowercase them.
- Use `re.sub()` to replace any `-` characters with spaces.
- Finally, use `str.join()` to combine all words using `-` as the separator.

```py
from re import sub

def snake(s):
  return '_'.join(
    sub('([A-Z][a-z]+)', r' \1',
    sub('([A-Z]+)', r' \1',
    s.replace('-', ' '))).split()).lower()
```

```py
snake('camelCase') # 'camel_case'
snake('some text') # 'some_text'
snake('some-mixed_string With spaces_underscores-and-hyphens')
# 'some_mixed_string_with_spaces_underscores_and_hyphens'
snake('AllThe-small Things') # 'all_the_small_things'
```


=======================
Test if some list elements are truthy

Checks if the provided function returns `True` for at least one element in the list.

- Use `any()` in combination with `map()` to check if `fn` returns `True` for any element in the list.

```py
def some(lst, fn = lambda x: x):
  return any(map(fn, lst))
```

```py
some([0, 1, 2, 0], lambda x: x >= 2 ) # True
some([0, 0, 1, 0]) # True
```

=======================
Sort list by indexes

 Sorts one list based on another list containing the desired indexes.

- Use `zip()` and `sorted()` to combine and sort the two lists, based on the values of `indexes`.
- Use a list comprehension to get the first element of each pair from the result.
- Use the `reverse` parameter in `sorted()` to sort the dictionary in reverse order, based on the third argument.

```py
def sort_by_indexes(lst, indexes, reverse=False):
  return [val for (_, val) in sorted(zip(indexes, lst), key=lambda x: \
          x[0], reverse=reverse)]
```

```py
a = ['eggs', 'bread', 'oranges', 'jam', 'apples', 'milk']
b = [3, 2, 6, 4, 1, 5]
sort_by_indexes(a, b) # ['apples', 'bread', 'eggs', 'jam', 'milk', 'oranges']
sort_by_indexes(a, b, True)
# ['oranges', 'milk', 'jam', 'eggs', 'bread', 'apples']
```


=======================
Sort dictionary by key

Sorts the given dictionary by key.

- Use `dict.items()` to get a list of tuple pairs from `d` and sort it using `sorted()`.
- Use `dict()` to convert the sorted list back to a dictionary.
- Use the `reverse` parameter in `sorted()` to sort the dictionary in reverse order, based on the second argument.

```py
def sort_dict_by_key(d, reverse = False):
  return dict(sorted(d.items(), reverse = reverse))
```

```py
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
sort_dict_by_key(d) # {'five': 5, 'four': 4, 'one': 1, 'three': 3, 'two': 2}
sort_dict_by_key(d, True)
# {'two': 2, 'three': 3, 'one': 1, 'four': 4, 'five': 5}
```


=======================
Sort dictionary by value

Sorts the given dictionary by value.

- Use `dict.items()` to get a list of tuple pairs from `d` and sort it using a lambda function and `sorted()`.
- Use `dict()` to convert the sorted list back to a dictionary.
- Use the `reverse` parameter in `sorted()` to sort the dictionary in reverse order, based on the second argument.
- **⚠️ NOTICE:** Dictionary values must be of the same type.

```py
def sort_dict_by_value(d, reverse = False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))
```

```py
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
sort_dict_by_value(d) # {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
sort_dict_by_value(d, True)
# {'five': 5, 'four': 4, 'three': 3, 'two': 2, 'one': 1}
```

=======================
Split into lines

Splits a multiline string into a list of lines.

- Use `str.split()` and `'\n'` to match line breaks and create a list.
- [`str.splitlines()`](https://docs.python.org/3/library/stdtypes.html#str.splitlines) provides similar functionality to this snippet.

```py
def split_lines(s):
  return s.split('\n')
```

```py
split_lines('This\nis a\nmultiline\nstring.\n')
# ['This', 'is a', 'multiline', 'string.' , '']
```

=======================
Spread list

Flattens a list, by spreading its elements into a new list.

- Loop over elements, use `list.extend()` if the element is a list, `list.append()` otherwise.

```py
def spread(arg):
  ret = []
  for i in arg:
    ret.extend(i) if isinstance(i, list) else ret.append(i)
  return ret
```

```py
spread([1, 2, 3, [4, 5, 6], [7], 8, 9]) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```


=======================
Sum list based on function

Calculates the sum of a list, after mapping each element to a value using the provided function.

- Use `map()` with `fn` to map each element to a value using the provided function.
- Use `sum()` to return the sum of the values.

```py
def sum_by(lst, fn):
  return sum(map(fn, lst))
```

```py
sum_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 20
```

=======================
Sum of powers

Returns the sum of the powers of all the numbers from `start` to `end` (both inclusive).

- Use `range()` in combination with a list comprehension to create a list of elements in the desired range raised to the given `power`.
- Use `sum()` to add the values together.
- Omit the second argument, `power`, to use a default power of `2`.
- Omit the third argument, `start`, to use a default starting value of `1`.

```py
def sum_of_powers(end, power = 2, start = 1):
  return sum([(i) ** power for i in range(start, end + 1)])
```

```py
sum_of_powers(10) # 385
sum_of_powers(10, 3) # 3025
sum_of_powers(10, 3, 5) # 2925
```


=======================
List symmetric difference based on function

Returns the symmetric difference between two lists, after applying the provided function to each list element of both.

- Create a `set` by applying `fn` to each element in every list.
- Use a list comprehension in combination with `fn` on each of them to only keep values not contained in the previously created set of the other.

```py
def symmetric_difference_by(a, b, fn):
  (_a, _b) = (set(map(fn, a)), set(map(fn, b)))
  return [item for item in a if fn(item) not in _b] + [item
          for item in b if fn(item) not in _a]
```

```py
from math import floor

symmetric_difference_by([2.1, 1.2], [2.3, 3.4], floor) # [1.2, 3.4]
```

=======================
List symmetric difference

Returns the symmetric difference between two iterables, without filtering out duplicate values.

- Create a `set` from each list.
- Use a list comprehension on each of them to only keep values not contained in the previously created set of the other.

```py
def symmetric_difference(a, b):
  (_a, _b) = (set(a), set(b))
  return [item for item in a if item not in _b] + [item for item in b
          if item not in _a]
```

```py
symmetric_difference([1, 2, 3], [1, 2, 4]) # [3, 4]
```


=======================
List tail

Returns all elements in a list except for the first one.

- Use slice notation to return the last element if the list's length is more than `1`.
- Otherwise, return the whole list.

```py
def tail(lst):
  return lst[1:] if len(lst) > 1 else lst
```

```py
tail([1, 2, 3]) # [2, 3]
tail([1]) # [1]
```

=======================
Remove list elements from the end

Returns a list with `n` elements removed from the end.

- Use slice notation to create a slice of the list with `n` elements taken from the end.

```py
def take_right(itr, n = 1):
  return itr[-n:]
```

```py
take_right([1, 2, 3], 2) # [2, 3]
take_right([1, 2, 3]) # [3]
```

=======================
Remove list elements

Returns a list with `n` elements removed from the beginning.

- Use slice notation to create a slice of the list with `n` elements taken from the beginning.

```py
def take(itr, n = 1):
  return itr[:n]
```

```py
take([1, 2, 3], 5) # [1, 2, 3]
take([1, 2, 3], 0) # []
```

=======================
Number to binary

Returns the binary representation of the given number.

- Use `bin()` to convert a given decimal number into its binary equivalent.

```py
def to_binary(n):
  return bin(n)
```

```py
to_binary(100) # 0b1100100
```


=======================
Lists to dictionary

Combines two lists into a dictionary, where the elements of the first one serve as the keys and the elements of the second one serve as the values.
The values of the first list need to be unique and hashable.

- Use `zip()` in combination with `dict()` to combine the values of the two lists into a dictionary.

```py
def to_dictionary(keys, values):
  return dict(zip(keys, values))
```

```py
to_dictionary(['a', 'b'], [1, 2]) # { a: 1, b: 2 }
```

=======================
Number to hex

Returns the hexadecimal representation of the given number.

- Use `hex()` to convert a given decimal number into its hexadecimal equivalent.

```py
def to_hex(dec):
  return hex(dec)
```

```py
to_hex(41) # 0x29
to_hex(332) # 0x14c
```

=======================
Date to ISO format

Converts a date to its ISO-8601 representation.

- Use `datetime.datetime.isoformat()` to convert the given `datetime.datetime` object to an ISO-8601 date.

```py
from datetime import datetime

def to_iso_date(d):
  return d.isoformat()
```

```py
from datetime import datetime

to_iso_date(datetime(2020, 10, 25)) # 2020-10-25T00:00:00
```


=======================
Integer to roman numeral

Converts an integer to its roman numeral representation.
Accepts value between `1` and `3999` (both inclusive).

- Create a lookup list containing tuples in the form of (roman value, integer).
- Use a `for` loop to iterate over the values in `lookup`.
- Use `divmod()` to update `num` with the remainder, adding the roman numeral representation to the result.

```py
def to_roman_numeral(num):
  lookup = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'),
  ]
  res = ''
  for (n, roman) in lookup:
    (d, num) = divmod(num, n)
    res += roman * d
  return res
```

```py
to_roman_numeral(3) # 'III'
to_roman_numeral(11) # 'XI'
to_roman_numeral(1998) # 'MCMXCVIII'
```

=======================
Transpose matrix


Transposes a two-dimensional list.

- Use `*lst` to get the provided list as tuples.
- Use `zip()` in combination with `list()` to create the transpose of the given two-dimensional list.

```py
def transpose(lst):
  return list(zip(*lst))
```

```py
transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# [(1, 4, 7, 10), (2, 5, 8, 11), (3, 6, 9, 12)]
```


=======================
Unfold list

Builds a list, using an iterator function and an initial seed value.

- The iterator function accepts one argument (`seed`) and must always return a list with two elements ([`value`, `nextSeed`]) or `False` to terminate.
- Use a generator function, `fn_generator`, that uses a `while` loop to call the iterator function and `yield` the `value` until it returns `False`.
- Use a list comprehension to return the list that is produced by the generator, using the iterator function.

```py
def unfold(fn, seed):
  def fn_generator(val):
    while True:
      val = fn(val[1])
      if val == False: break
      yield val[0]
  return [i for i in fn_generator([None, seed])]
```

```py
f = lambda n: False if n > 50 else [-n, n + 10]
unfold(f, 10) # [-10, -20, -30, -40, -50]
```


=======================
List union based on function


Returns every element that exists in any of the two lists once, after applying the provided function to each element of both.

- Create a `set` by applying `fn` to each element in `a`.
- Use a list comprehension in combination with `fn` on `b` to only keep values not contained in the previously created set, `_a`.
- Finally, create a `set` from the previous result and `a` and transform it into a `list`

```py
def union_by(a, b, fn):
  _a = set(map(fn, a))
  return list(set(a + [item for item in b if fn(item) not in _a]))
```

```py
from math import floor

union_by([2.1], [1.2, 2.3], floor) # [2.1, 1.2]
```

=======================
List union

Returns every element that exists in any of the two lists once.

- Create a `set` with all values of `a` and `b` and convert to a `list`.

```py
def union(a, b):
  return list(set(a + b))
```

```py
union([1, 2, 3], [4, 3, 2]) # [1, 2, 3, 4]
```

=======================
Unique elements in list

Returns the unique elements in a given list.

- Create a `set` from the list to discard duplicated values, then return a `list` from it.

```py
def unique_elements(li):
  return list(set(li))
```

```py
unique_elements([1, 2, 2, 3, 4, 3]) # [1, 2, 3, 4]
```

=======================
Dictionary values

Returns a flat list of all the values in a flat dictionary.

- Use `dict.values()` to return the values in the given dictionary.
- Return a `list()` of the previous result.

```py
def values_only(flat_dict):
  return list(flat_dict.values())
```

```py
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
values_only(ages) # [10, 11, 9]
```

=======================
Weighted average

Returns the weighted average of two or more numbers.

- Use `sum()` to sum the products of the numbers by their weight and to sum the weights.
- Use `zip()` and a list comprehension to iterate over the pairs of values and weights.

```py
def weighted_average(nums, weights):
  return sum(x * y for x, y in zip(nums, weights)) / sum(weights)
```

```py
weighted_average([1, 2, 3], [0.6, 0.2, 0.3]) # 1.72727
```

=======================
Apply function when true

Tests a value, `x`, against a testing function, conditionally applying a function.

- Check if the value of `predicate()` is `True` for `x` and if so call `when_true()`, otherwise return `x`.

```py
def when(predicate, when_true):
  return lambda x: when_true(x) if predicate(x) else x
```

```py
double_even_numbers = when(lambda x: x % 2 == 0, lambda x : x * 2)
double_even_numbers(2) # 4
double_even_numbers(1) # 1
```

=======================
String to words

Converts a given string into a list of words.

- Use `re.findall()` with the supplied `pattern` to find all matching substrings.
- Omit the second argument to use the default regexp, which matches alphanumeric and hyphens.

```py
import re

def words(s, pattern = '[a-zA-Z-]+'):
  return re.findall(pattern, s)
```

```py
words('I love Python!!') # ['I', 'love', 'Python']
words('python, javaScript & coffee') # ['python', 'javaScript', 'coffee']
words('build -q --out one-item', r'\b[a-zA-Z-]+\b')
# ['build', 'q', 'out', 'one-item']
```


=======================








