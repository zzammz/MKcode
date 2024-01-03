
===================
Calculates the date of n days from the given date.

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
=====================
Checks if all elements in a list are equal.

Use set() to eliminate duplicate elements and then use len() to check if length is 1.

```py
def all_equal(lst):
  return len(set(lst)) == 1


all_equal([1, 2, 3, 4, 5, 6]) # False
all_equal([1, 1, 1, 1]) # True

```

============================
Checks if all the values in a list are unique.

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

======================
arithmetic progression

Generates a list of numbers in the arithmetic progression starting with the given positive integer and up to the specified limit.

Use range() and list() with the appropriate start, step and end values.

```py
def arithmetic_progression(n, lim):
  return list(range(n, lim + 1, n))
arithmetic_progression(5, 25) # [5, 10, 15, 20, 25]
```

=======================
Mapped list average


Calculates the average of a list, after mapping each element to a value using the provided function.

Use map() to map each element to the value returned by fn.
Use sum() to sum all of the mapped values, divide by len(lst).
Omit the last argument, fn, to use the default identity function.


```py
def average_by(lst, fn = lambda x: x):
  return sum(map(fn, lst), 0.0) / len(lst)
```

```py
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





=======================





=======================





=======================







=======================





=======================





=======================





=======================







=======================





=======================





=======================





=======================







=======================





=======================





=======================





=======================







=======================





=======================





=======================





=======================





