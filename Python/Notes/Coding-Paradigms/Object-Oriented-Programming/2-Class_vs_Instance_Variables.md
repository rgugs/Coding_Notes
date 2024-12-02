# Class vs Instance Variables

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Class vs Instance Variables](#class-vs-instance-variables)
  - [When to use Class variable?](#when-to-use-class-variable)
  - [Scope](#scope)
  - [Instance Variable](#instance-variable)
  - [Sources](#sources)

<!-- /code_chunk_output -->


When we wrote our 1st class, we used class variables, and with the init method we can now make instance variables. What is the difference? Class variable are the same for every instance while instance variable are unique to each instance. 

There are a few pitfalls you need to watch out for when using this type of logic. Let's say we want to make a class of Dog. Every dog can learn tricks, so we make a class variable list of tricks. This is wrong. Why? Coding it like this would mean that every dog created from this class shares this same list of tricks. This could be an interesting use of of a class variable for a telepathic alien dog race, but it not how we expect it to work here on Earth. Instead, create the tricks list as an instance variable.

<table>
<tr>
<th>Wrong</th><th>Correct</th>
</tr>
<tr>
<td>

```python
class Dog:
    tricks = []
    def __init__(self, name):
        self.name = name

    def add_tricks(self, trick):
        self.tricks.append(trick)
```

</td>
<td>

```python
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_tricks(self, trick):
        self.tricks.append(trick)

```

</td>
</tr>
</table>

## When to use Class variable?

Other than for a telepathic alien example, when would we want to use a class variable instead of an instance variable?

One simple example could be a small business employee tracking system. If every year all employees get the same percentage of raise, a class variable could be useful here.

Here is our Employee class with a class variable for the raise amount:

```python
class Employee:
    raise_amount = 1.04 # 4% raise

    def __init__(self, first, last, pay):
        self.firstname = first
        self.lastname = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

    def fullname(self):
        return f'{self.firstname} {self.lastname}'
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)    # Access class variable with Employee.raise_amount

emp1 = Employee('Bob', 'Jones', 40000)
emp2 = Employee('Susan', 'Smith', 50000)
emp3 = Employee('Kelly', 'Stone', 60000)

print('Before Raise:')
print(f'{emp1.fullname()} pay: {emp1.pay}') # Bob Jones pay: 40000
print(f'{emp2.fullname()} pay: {emp2.pay}') # Susan Smith pay: 50000
print(f'{emp3.fullname()} pay: {emp3.pay}') # Kelly Stone pay: 60000
print(' ')

# End of year raise
emp1.apply_raise()
emp2.apply_raise()
emp3.apply_raise()

print('After Raise:')
print(f'{emp1.fullname()} pay: {emp1.pay}') # Bob Jones pay: 41600
print(f'{emp2.fullname()} pay: {emp2.pay}') # Susan Smith pay: 52000
print(f'{emp3.fullname()} pay: {emp3.pay}') # Kelly Stone pay: 62400
```

This seems like a solid design choice if we never ever plan to give differnt sizes of raises to different employees, but what if we want to switch our raise amount to be tied to personal performance reviews instead? In that case, the below code would be better. Can you spot the difference?

```python
class Employee:
    raise_amount = 1.04 # 4% raise

    def __init__(self, first, last, pay):
        self.firstname = first
        self.lastname = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

    def fullname(self):
        return f'{self.firstname} {self.lastname}'
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)    # Access instance variable with self.raise_amount

emp1 = Employee('Bob', 'Jones', 40000)
emp2 = Employee('Susan', 'Smith', 50000)
emp3 = Employee('Kelly', 'Stone', 60000)

print('Before Raise:')
print(f'{emp1.fullname()} pay: {emp1.pay}') # Bob Jones pay: 40000
print(f'{emp2.fullname()} pay: {emp2.pay}') # Susan Smith pay: 50000
print(f'{emp3.fullname()} pay: {emp3.pay}') # Kelly Stone pay: 60000
print(' ')

# End of year raise
emp1.apply_raise()
emp2.apply_raise()
emp3.apply_raise()

print('After Raise:')
print(f'{emp1.fullname()} pay: {emp1.pay}') # Bob Jones pay: 41600
print(f'{emp2.fullname()} pay: {emp2.pay}') # Susan Smith pay: 52000
print(f'{emp3.fullname()} pay: {emp3.pay}') # Kelly Stone pay: 62400
```

We've switched Employee.raise_amount to `self.raise_amount` instead. The code currently performs exactly the same because of scope in Python.

## Scope

Python scope goes from inner to outer, so it will first try to reference a variable name in the inner most scope, in this case the instance, and then it will look a step up in the class. It found a matching variable there, so it stops looking, but if a variable wasn't found there, it would continue to an outer step and check for a global variable. Setting things as an instance variable leaves more flexibility for differences between instances than a class variable will.

## Instance Variable

What if Susan has an excellent review, Kelly is standard, and Bob is not doing well and is placed on a PIP (Performance Improvement Plan)? According to our new desire to give raises based on performance, Kelly gets the standard 4% raise, Susan gets a 5% raise, and Bob gets a 3% raise.

```python
print('Before Raise:')
print(f'{emp1.fullname()} pay: {emp1.pay}')
print(f'{emp2.fullname()} pay: {emp2.pay}')
print(f'{emp3.fullname()} pay: {emp3.pay}')
print(' ')

# Set individual raise amount
emp1.raise_amount = 1.03
emp2.raise_amount = 1.05
emp3.raise_amount = 1.04    # We could leave the blank as well, since it matches the Class variable amount. Comment it out and try running it without setting it.

# End of year raise
emp1.apply_raise()
emp2.apply_raise()
emp3.apply_raise()

print('After Raise:')
print(f'{emp1.fullname()} pay: {emp1.pay}') # Output: Bob Jones pay: 41200
print(f'{emp2.fullname()} pay: {emp2.pay}') # Output: Susan Smith pay: 52500
print(f'{emp3.fullname()} pay: {emp3.pay}') # Output: Kelly Stone pay: 62400
```

## Sources

Corey Schafer
https://www.youtube.com/watch?v=BJ-VvGyQxho&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=2