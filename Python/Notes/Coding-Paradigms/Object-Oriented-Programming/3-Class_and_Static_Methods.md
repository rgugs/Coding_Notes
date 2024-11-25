# Class and Static Methods

Regular methods in a class automatically take the instance as the first argument (self).

How do we change it so it takes the class first? Turn a regular method into a **class method**. To do this, we'll use a decorator.

```python
class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f'{self.first}.{self.last}@company.com'
        self.pay = pay
    
    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount  # Changes raise_amt for every instance in class
```

## Class Methods as Alternative Constructors

What is an alternative constructor? In the example above, our class requires a first name (str), last name(str), and pay(int) to construct the class, but what if you commonly get the information for each instance as a list or tuple instead of as individual values? You will need to unpack that information first to use it to make an instance. By using and Alternative Constructur, you can move that unpacking to a class method instead of separate functions so you know to update one if the other updates.

The common verbiage for these constructors is to include "from" in the name, such as "from_string" or "from_csv".

```python
@classmethod
def from_string(cls, emp_string):
    first, last, pay = emp_string.split('-')
    return cls(first, last, pay)

new_emp_1 = Employee.from_string(emp_string_1)
```

Examples of this can be seen in the datetime module and is common in Pandas as well.

## Static Methods

All regular methods in a class pass the instance (self) into the method as the first argument, and class methods will pass the class into the method as the first argument, but what if you don't actually need to access either the instance or the class? This is called a static method, and they don't pass anything first into the method. They behave like regular functions, but are included in the class because they have some logical connection to it.

Let's say we want a simple function that will take in a date and check if that day is a work day or a weekend day. In Python, days of the week have #'s with Monday being 0 to Sunday being 6.

```python
import datetime

my_date = datetime.date(2016, 07, 10)

@staticmethod   # Decorator
def isworkday(day):
    if day.weekday > 4:
        return False
    Return True
```

## Sources

Corey Schafer
<https://www.youtube.com/watch?v=rq8cL2XMM5M&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=3>
