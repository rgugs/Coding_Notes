# Classes

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
https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=40

Boot.dev

TechTarget
https://www.techtarget.com/searchapparchitecture/definition/object-oriented-programming-OOP#:~:text=An%20object%20can%20be%20defined,and%20actively%20updated%20or%20maintained.