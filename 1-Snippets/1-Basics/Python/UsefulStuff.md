
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


```p
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


