# Encapsulation in OOP

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Encapsulation in OOP](#encapsulation-in-oop)
  - [Protected](#protected)
  - [Private](#private)
  - [Dunder/Magic/Special Methods vs Name Mangling](#dundermagicspecial-methods-vs-name-mangling)
  - [Sources](#sources)

<!-- /code_chunk_output -->

Encapsulation in OOP focuses on hiding data and complexity from the users of the code. While Python is based on OOP in that everything in it is an object, it does not have true encapsulation with enforced public and private attributes/methods. It does have some standards that developers should view as best practices to follow.

## Protected

Using a single underscore indicates to developers the attribute or method is considered *"protected"* and they should avoid calling it directly using dot notation. Should does not mean can't. It will show up if a developer uses the .__dict__ option, so it is not hidden from use. It is still possible to access and change the variable value outside of the class using dot notation if you know the variable exists.

**Use when you want to allow subclasses to access and potentially override attributes or methods while still signaling that they are part of the internal implementation.**

```python
class Animal:
    def __init__(self, name, species):
        self.name = name    # public attribute
        self._species = species      # "protected" attribute

wilbur = Animal("Wilbur", "pig")
print(wilbur.__dict__)  # Output: {'name': 'Wilbur', '_species': 'pig'
print(wilbur.name)      # Output: Wilbur
print(wilbur._species)  # Output: pig
```

## Private

As mentioned above, Python does not have true private variables/methods like other OOP languages such as Java, but developers can use **Name Mangling** to increase the warning to other developers that this is a private method. Name Mangling is something Python does when it encounters an attribute/method reference that starts with double underscores. The attribute or method is prefixed by the class name and a single leading underscore. This prevents issues with methods and functions that use the same name by ensuring they are class specific. The main use for this is to avoid name collisions when dealing with class inheritance, to ensure an attribute isn't overwritten in a subclass. We can also use it for private methods.

**Use for attributes or methods that are truly internal to the class and should not be accessed or modified directly from outside.**

```python
class Animal:
    def __init__(self, name):
        self.name = name    # public attribute
        self._species = "pig"     # "protected" attribute
        self.__accommodation = "barn" # "private" attribute


wilbur = Animal("Wilbur", "pig")
print(wilbur.__dict__)  # Output: {'name': 'Wilbur', '_species': 'pig'
print(wilbur.name)      # Output: Wilbur
print(wilbur._species)  # Output: pig

print(wilbur.__accommodation)   # AttributeError: 'Animal' object has no attribute '__accommodation'

print(wilbur.__dict__)  # Output: {'name': 'Wilbur', '_species': 'pig', '_Animal__accommodation': 'barn'}
print(wilbur._Animal__accommodation)    # Output: barn
```

In the code above, you can see that we can still see all the types of attributes when using `wilbur.__dict__`, so none of the information is actually hidden. We can no longer access the attribute directly with `wilbur.__accommodation`, but we can still access it if we included the name mangled version of `wilbur._Animal__accommodation`, and it can still be changed as well.

## Dunder/Magic/Special Methods vs Name Mangling

Dunder Methods also use double underscore, but should not be confused with name mangling. They refer to specific class methods that start and end with double underscores, including `__init__()`, `__repr__()`, and `__eq__()`. These functions are already set for the built in python class types, but must be set by the developer for custom classes if that functionality is desired. They are used to customize the behavior of classes.

## Sources

Boot.dev
<https://www.boot.dev/lessons/6cd6445f-6226-4a98-a9f9-ee03e07cf37c>

Bitfumes
<https://www.youtube.com/watch?v=GN1LR0UoFI4&t=191s>

Pylenin
<https://www.youtube.com/watch?v=pYctrJgfQEY>

ArjanCodes
<https://www.youtube.com/watch?v=29NMlHHLUsI>
