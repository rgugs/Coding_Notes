# Decorators : ***IN PROGRESS***

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Decorators : ***IN PROGRESS***](#decorators--in-progress)
  - [Review First Class Functions and Closures](#review-first-class-functions-and-closures)
    - [Closure Example](#closure-example)
  - [What is a Decorator?](#what-is-a-decorator)
    - [Decorators without Arguments Example](#decorators-without-arguments-example)
    - [The @ Syntax](#the--syntax)
    - [Decorators with Arguments Example](#decorators-with-arguments-example)
  - [Useful Built In Decorators](#useful-built-in-decorators)
    - [@property](#property)
    - [@staticmethod](#staticmethod)
    - [@classmethod](#classmethod)
    - [functools.cache](#functoolscache)
    - [@dataclass](#dataclass)
  - [Sources](#sources)

<!-- /code_chunk_output -->

Decorators are a feature in Python that I only recently started to see as I moved into more intermediate usage. In my case, I was working through learning OOP (Object Oriented Programming) in Python and I kept running into examples using @dataclass and @abstractmethod. What are these fancy things, I wondered. I finally found a really clear video explaining the what, how, and why of decorators in Corey Schafer's Decorator's video. It was made in 2016, but as of now (11/18/2024) it still holds true and really helped me work through this topic so I can get back to learning OOP.

## Review First Class Functions and Closures

If you don't know what a **First Class Function** or a **Closure** is, here is a very short review, but please refer to the notes and sources for those specific topics for more indepth understanding.

>**First Class Functions** - Treat functions like any other object. Can pass functions as arguments to another function, return functions, and assign functions to variables.

>**Closures** - Build on 1st class functions by returning an inner function that remembers and has access to variable local to the scope in which they were created.

### Closure Example

```python
def outer_function():
    message = 'Hi!' # Free variable - variable that is used in a code block (like a function) but is not defined within that block. Instead, it is defined in an outer scope.
    def inner_function():
        print(message)
    return inner_function   # Lack of parentheses means function won't run yet. Returns function to assigned variable instead of running immediately.

my_func = outer_function()
my_func()   # Output: Prints 'Hi!'
```

## What is a Decorator?

>**Decorator** - Function that takes another function as an argument, adds functionality, and returns another function without altering source code of the original function.

Why would we want this functionality? Several real world examples include logging, timing, or caching.

### Decorators without Arguments Example

In the code below, an outer function that is the decorator function accepts an original function as an argument. Inside the decorator function is the wrapper function that in later examples you will see executes other code, then runs the original function. When the decorator function is assigned to a variable, that variable becomes the wrapper function, so when it is executed, it completes its code before running the original function code.

```python
def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function # No parentheses means the function won't execute yet

def display():
    print('display function ran')

decorated_display = decorator_function(display)
decorated_display() # Runs the wrapper function, which runs the original function
```

### The @ Syntax

The most common way to use a decorator function, either a custom or built in one, is to use the `@example_decorator` syntax. This looks much cleaner than assigning multiple functions to other functions, especially when stacking the decorators, which is covered later. These sets of code have different syntax, but accomplish the same task using the decorator function defined above.

<table>
<tr>
<td>Original Format</td><td>@ Format</td>
</tr>
<tr>
<td>

```python
def display():
    print('display function ran')

decorated_display = decorator_function(display)
decorated_display()
```

</td>
<td>

```python
@decorator_function
def display():
    print('display function ran')

display()
```

</td>
</tr>
</table>

### Decorators with Arguments Example

The above decorator works with functions without any arguments, but what if you want to use it with any function any time that may have any number of arguments? For that we need to add `*args and **kwargs` inside the parentheses.

>`*args` - Includes any positional arguments that must be passed into the function in a specific order (name, age)
>
>`**kwargs` - Includes any keyword arguments that may be passed into the function in any order when set with the keyword. (age=12, name='Brenna')

```python
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):  # Allows passing the arguments in when setting up the function
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)   # Runs the original function with the passed in arguments.
    return wrapper_function

@decorator_function
def display():
    print('display function ran')

@decorator_function
def display_info(name, age):
    print(f'display_info ran with arguments({name}, {age})')

display() # Output: display function ran

display_info('John', 25)

# Output:
# wrapper executed this before display_info
# display info ran with arguments (John, 25)
```

As you can see, both functions with and without arguments ran correctly using the same decorator function.

## Useful Built In Decorators

1. @property
2. @staticmethod
3. @classmethod
4. functools.cache
5. @dataclass

### @property

### @staticmethod

### @classmethod

### functools.cache

### @dataclass

## Sources

Corey Schafer - Decorators
<https://www.youtube.com/watch?v=FsAPt_9Bf3U&t=1s>

Omri Grossman - Why Use Python Dataclass (decorator)
<https://dev.to/omrigm/why-you-should-use-python-data-classes-48po>

Abhishek Jain
<https://medium.com/@abhishekjainindore24/embracing-abstraction-a-dive-into-abstract-classes-in-python-0faf6d83948d>

Natalia Tsarkova - Why do we need Decorators?
<https://medium.com/exness-blog/why-do-we-need-decorators-use-cases-13f19ca5d237>

Estefania Cassingena Navone
<https://www.freecodecamp.org/news/python-property-decorator/>
