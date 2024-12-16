# Python Closures

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Python Closures](#python-closures)
  - [Scope in Python Review](#scope-in-python-review)
  - [Closure Walkthrough](#closure-walkthrough)
  - [Sources](#sources)

<!-- /code_chunk_output -->

**Closure** - Function object that remembers values in enclosing scopes even if they are not present in memory. **--Better Definition--** is a nested function that allows us to access variables of the outer function even after the outer function is closed.

## Scope in Python Review

Just a quick review on scope, Like a set of nesting dolls, Python has varying levels of scope. When passed a variable, Python starts checking in the "lowest" level of scope, the local scope, then moves outwards, so inner scopes can access outer scopes, but outer scopes can't access inner scopes.

## Closure Walkthrough

In the example below we have a higher order function with and outer and inner function. The inner function is the closure. When we first call the outer function, we are assigning the inner function to the variable, but also passing it the argument originally put into the outer function. The Closure is special in that even after the outer function has finished running, the inner function can still use the arguement that was passed to it. The inner function is effectively being modified so that if the passed in x variable was 10, then the inner_function would be returning `10 + y` instead of `x + y`.

```python
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(5) # x is 5
print(closure(3))   # y is 5 Output: 8
```

Another example is this logger example first seen in the First Class Functions lesson.

The logger function is passed a message variable that is set when the closure is assigned to a variable. That variable is used in the inner log_message function when it is print out.

```python
def logger(msg):
    def log_message():
        print(f'Log: {msg}')
    return log_message

log_hi = logger('Hi!')
log_hi()    # Prints 'Log: Hi!'
```

## Sources

Geeks for Geeks - Scope Review
<https://www.geeksforgeeks.org/scope-resolution-in-python-legb-rule/>

Corey Schafer - Closures
<https://www.youtube.com/watch?v=swU3c34d2NQ&t=8s>

Corey Schafer YouTube - First Class Functions
<https://www.youtube.com/watch?v=kr0mpwqttM0&t=5s>