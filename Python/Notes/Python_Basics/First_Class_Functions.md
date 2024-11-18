# First Class Functions in Python

What does it mean when something is referred to as a first class citizen in programming, and why is are we learning about it?

> **First Class Citizen (Programming)** - Entity which supports all the operations generally available to other entities. These operations typically include being passed as an argument, returned from a function, and assigned to a variable.
>  
> **First Class Function** - When a function is treated as a first class citizen in programming.

Unstanding that we can do all the things you can do with any other variable you might be familiar with allows us to create code that is more flexible and modular. This makes our code less likely to break and easier to test. First order functions are used in both Object Oriented Programming and Functional Programming.

If you've already covered some basic python, you've probably seen a function assigned to a variable.

```python
def square(x):
    return x * x

f = square(5)   # Assigns result of function to variable
```

However if we remove the parentheses, the function won't run immediately and instead of assigning the result of the function to the variable, we assign the function to the variable itself.

```python
f = square

a = f(5)    # same as if we did a = square(5) now
```

## Higher Order Functions

By passing one function into another function, you will create **Higher Order Function**.

**Higher Order Functions** - Pass functions as arguments and return functions as results of other functions.

Why should we create higher order functions? It hides complexity and makes code more readable. You've probably used a higher order function before without even realizing it.

## Higher Order Function Examples

Commonly used built in higher order functions in Python include map(), filter(), reduce(), zip(), and sorted(). You can also create custom higher order functions, such as the custom map function example below. **Lambdas** (unnamed functions with a single expression) are commonly used in higher order functions.

### Custom Map

```python
def square(x):
    return x * x

def cubed(x):
    return x * x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))

    return result

num_list = [1, 2, 3, 4, 5]

squares = my_map(square, num_list)  # Output: [1, 4, 9, 16, 25]

cubes = my_map(cube, num_list)  # Output: [1, 8, 27, 64, 125]
```

### Built in Filter

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))  # Output: [2, 4, 6, 8]
```

## Sources

Corey Schafer YouTube - First Class Functions
https://www.youtube.com/watch?v=kr0mpwqttM0&t=5s

Free Code Camp
https://www.freecodecamp.org/news/first-class-functions-and-closures-in-python/

Python Documentation
https://docs.python.org/3/library/functions.html
