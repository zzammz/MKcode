
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


