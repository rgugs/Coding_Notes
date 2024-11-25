# Function vs Method

Something that confused me early on whas the difference between functions and methods and how to use them. Methods are functions that exist inside a class, and the method is specifically being called on the instance with dot notation. Sorted() and list.sort() are examples of functions and methods. When trying to determine if something is a function or method, look at how it is written.

## Sorted()

Sorted() is a built in Python function and can take **any iterable** (list, set, dictionary, tuple) and return the values as a new sorted list,
so the original iterable is not changed. If you pass a non list iterable into Sorted(), you must **cast** it back into the desired format if
you don't want to end up with a list.

## List.sort()

In comparison, the list.sort() method only works on lists and also sorts them in place, meaning it will change the original variable.
If you don't want that to happen, you will have to first use list.copy() to copy the list to a new variable. You can apply multiple
methods to an object in a single line, however you need to consider what each method returns. In the case below, you can't use
chaining because you need .sort() to apply to the new_list object, not the original list object.

```python
# Sorted()
new_list = sorted(list)

# List.sort()
new_list = list.copy()
new_list.sort()
```
