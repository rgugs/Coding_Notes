# First Class Functions in Python

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [First Class Functions in Python](#first-class-functions-in-python)
  - [Higher Order Functions](#higher-order-functions)
  - [Higher Order Function Examples](#higher-order-function-examples)
    - [Custom Map](#custom-map)
    - [Built in Filter()](#built-in-filter)
    - [Logging Example](#logging-example)
    - [Tag Wrapping](#tag-wrapping)
  - [Sources](#sources)

<!-- /code_chunk_output -->

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

Commonly used built in higher order functions in Python include map(), filter(), reduce(), zip(), and sorted(). You can also create custom higher order functions, such as the custom map function example below. **Lambdas** (unnamed functions with a single expression) are commonly used in higher order functions. Other real world uses include logging or timing higher functions.

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

### Built in Filter()

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))  # Output: [2, 4, 6, 8]
```

### Logging Example

This example is a **Closure**, which will be covered in depth in a different lesson.

```python
def logger(msg):
    def log_message():
        print(f'Log: {msg}')
    return log_message

log_hi = logger('Hi!')
log_hi()    # Prints 'Log: Hi!'
```

In the code above, we've created a higher order function called `logger` that has a 2nd function inside it, called `log_message`. When you write `log_hi = logger('Hi!')` you are assigning the interior function to the variable while passing the message through the outer function, so the outer function runs at the time of assignment, but not the interior function. When you write `log_hi()`, the `()` tell python to run the function, and you get the final out put with the log message and the previously input text.

### Tag Wrapping

This is an example of using a higher function to set HTML brackets.

```python
def html_tag(tag):
    def wrap_text(msg):
        print(f'<{tag}>{msg}</{tag}>')
    return wrap_text

print_h1 = html_tag('h1')
print_p = html_tag('p')

print_h1('Test Headline')   # Output: <h1>Test Headline</h1>
print_p('Test Paragragh')   # Output: <p>Test Paragraph</p>
```

## Sources

Corey Schafer YouTube - First Class Functions
<https://www.youtube.com/watch?v=kr0mpwqttM0&t=5s>

Free Code Camp
<https://www.freecodecamp.org/news/first-class-functions-and-closures-in-python/>

Python Documentation
<https://docs.python.org/3/library/functions.html>
