# Type of Loops

## For Loops

For loops are used for iterating over a sequence, usually the number of items in and iterable such as a list or dictionary, but can also be used to iterate a set number of times using the range() function.

`for i in range(<number of iterations>):` - Iterates the number of times set inside the range function

`for i in items:` - Assuming items is a variable storing an iterable like a list or dictionary, it will iterate through each item in the iterable.

`for key, value in dictionary.items():` - Unpacks the key and value from a dictionary into variables for each item in the dictionary.

## While Loops

While loops repeat a block of code while a specific condition remains true. This can lead to infinite loops if you aren't careful.

```python
counter = 5
while counter > 5:
counter -= 1
```
