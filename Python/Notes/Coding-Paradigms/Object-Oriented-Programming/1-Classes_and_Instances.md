# Classes

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Classes](#classes)
  - [Definitions](#definitions)
  - [Building a Python Class](#building-a-python-class)
    - [Attribute References](#attribute-references)
    - [Methods](#methods)
    - [Function vs Method](#function-vs-method)
      - [Sorted()](#sorted)
      - [List.sort()](#listsort)
  - [Instantiation](#instantiation)
  - [Sources](#sources)

<!-- /code_chunk_output -->

## Definitions

> *Class* - A "blueprint" that defines the kind of data the associated objects contain and any logic sequences that can manipulate that type of object.
>
> *Object* - A data field that has unique attributes and behavior (eg.The number 12 or the name Fred.)
>
> *Instance* - Considered synonymous with objects, instances refer to an object created with a specific class type. (eg. 12 -> integer (number) or Fred -> string (name))

Python is an Object Oriented Programming language (OOP). Nearly everything in Python is an object, and objects are created as instances of a Class. This means that even if you prefer to use a programming model other than OOP, you still need to understand Classes in Python to use the Classes that are included with Python or found in external libraries.

The syntax for writing classes in Python is to use uppercase letters at the start of each word and no underscores between words. This is called CapWords or PascalCase.

***Python does not enforce these rules, but they are best practices and make your code more readable.***

```python
# Correct
class Animal:
    pass

class SmallTown:
    pass

# Incorrect
class big_farm:
    pass
```

## Building a Python Class

### Attribute References

Let's build our first class. We'll add 2 class attributes, type and name.

```python
class Animal:
    type = 'pig'
    name = 'Wilbur'
```

Now we'll create our first Animal object.

```python
animal_1 = Animal()

# Check object attributes using dot notation

print(animal_1.type)
print(animal_1.name)
```

You can change the assigned attribute values if the attribute is writable or add new attributes to the object. Writable attributes can also be deleted.

```python
animal_1.type = 'goat'
animal_1.age = 1
del animal_1.age
```

### Methods

So far we've covered adding *attribute refernces* to a class, but functions can also be attribute references. When functions are placed inside a class, they are referred to as **methods** and are limited in scope compared to functions outside the Class. They work on a specific instance of the Class and use dot notation, the same way you can access other object attributes.

```python
class Animal:
    name = 'Wilbur'

    def sleep(self):
        print('Wilbur is sleeping...')

animal_1 = Animal()
animal_1.sleep()    # Output: prints 'Wilbur is sleeping...' to terminal
```

### Function vs Method

Something that confused me early on was the difference between functions and methods and how to recognize and use them. All methods are functions, but not all functions are methods. Methods are functions that exist inside a class, and the method is specifically being called on the instance with dot notation. Sorted() and list.sort() are examples of a functions and method, respectively, that accomplish similar tasks. When trying to determine if something is a function or method, look at how it is written. If you are using dot notation `list_example.sort()`, it's a method, and you are applying that method specifically to that instance of a list object. (Datatypes in Python are all objects made with that specific datatype class.) If the datatype you are trying to sort is inside the parentheses instead of using dot notation like `new_list = sorted(list_example)`, you are applying a function that is outside of a class.

#### Sorted()

Sorted() is a built in Python function and can take **any iterable datatype** (list, set, dictionary, tuple) and return the values as a new sorted list, so the original iterable object is not changed. If you pass a non list iterable into Sorted(), you must assign it to a new variable and then **cast** it back into the desired datatype format if you don't want to end up with a list.

>This is an example of **abstraction**, where it takes the relatively common task of inputing a data type, converting it to a list, sorting it, and then returning the list and combines it into a single built in function instead of developers having to write their own versions of that over and over again.

#### List.sort()

In comparison, the list.sort() method only works on lists and also sorts them in place, meaning it will change the original variable. If you don't want that to happen, you will have to first use list.copy() to copy the list to a new variable. You can apply multiple methods to an object in a single line, however you need to consider what each method returns. In the case below, you can't use chaining because you need .sort() to apply to the new_list object, not the original list object.

```python
cars = ['BMW', 'Toyota', 'Honda', 'Audi']

new_list = sorted(cars)

print(f'Original list: {cars}')    # Original list: ['BMW', 'Toyota', 'Honda', 'Audi']
print(f'New list 1: {new_list}')    # New list 1: ['Audi', 'BMW', 'Honda', 'Toyota']

new_list2 = cars.copy().sort()

print(f'Original list: {cars}')     # Original list: ['BMW', 'Toyota', 'Honda', 'Audi']
print(f'New list 2: {new_list2}')   # New list 2: None

new_list3 = cars.copy()
new_list3.sort()

print(f'Original list: {cars}')     # Original list: ['BMW', 'Toyota', 'Honda', 'Audi']
print(f'New list 3: {new_list3}')   # New list 3: ['Audi', 'BMW', 'Honda', 'Toyota']
```

## Instantiation

So far we've set up class attributes that any instance of that class can access, but it is not dynamic. To create a class that can take different variable at creation time, we need to use one of the **Magic Methods** associated with classes. These are also called **Dunder Methods**, for double underscore, or **Special Methods**.

```python
# Initialize Dunder/Magic/Special Method
class Animal:    
    def __init__(self):
        pass
```

While most functions and methods must be specifically called to run, the init method is different. It runs automatically when the class object is instantiated (`animal_1 = Animal()`). You can add in different variable or methods to run inside this method to complete a complex object without having to run those commands for every instance after creation.

The first variable in the init method is always self. You can think of it as making the object self-aware. Just like any other function, you add in variables into the parentheses, and then instead of hard coding information, you assign those variables to the object's self. You don't need to include 'self' when assigning attributes.

```python
class Animal:
    def __init__(self, type, name):
        self.type = type
        self.name = name
```

Now instead of creating multiple copies of Wilbur the Pig, you can create a whole farm of animals!

```python
class Animal:
    def __init__(self, type, name):
        self.type = type
        self.name = name

animal_1 = Animal('pig', 'Wilbur')
animal_2 = Animal('goat', 'Freddie')
animal_3 = Animal('dog', 'Lily')

print(f'{animal_1.name} is a {animal_1.type}.') # Output: 'Wilbur is a pig.'
print(f'{animal_2.name} is a {animal_2.type}.') # Output: 'Freddie is a goat.'
print(f'{animal_3.name} is a {animal_3.type}.') # Output: 'Lily is a dog.'
```

## Sources

Corey Schafer
<https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=40>

Boot.dev
<https://www.boot.dev/lessons/ea171b42-0d9b-43d2-a136-4e2e89227f9e>

TechTarget
<https://www.techtarget.com/searchapparchitecture/definition/object-oriented-programming-OOP#:~:text=An%20object%20can%20be%20defined,and%20actively%20updated%20or%20maintained.>
