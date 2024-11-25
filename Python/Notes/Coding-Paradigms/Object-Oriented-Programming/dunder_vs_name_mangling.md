# Dunder/Magic/Special Methods vs Name Mangling

Dunder Methods refers to specific class methods that start and end with double underscores, including `__init__()`, `__repr__()`, and `__eq__()`. These functions are already set for the built in python class types, but must be set by the developer for custom classes if that functionality is desired.

Name Mangling is something Python does when it encounters an attribute reference that starts with double underscores. The attribute or method is prefixed by the class name and a single leading underscore. This prevents issues with methods and functions that use the same name by ensuring they are class specific. The main use for this is to avoid name collisions when dealing with class inheritance, to ensure an attribute isn't overwritten in a subclass.

```python
class MyClass:
    def __init__(self, attribute):
        self.__attribute = attribute

x = MyClass(attribute)
```

Attributes that start with underscores are sometimes called Private attributes, however Python does not have enforced private vs public attributes and if you know it exists, you could still call the attribute up using `x._MyClass__attribute` in the example above.

Best practice is to use a leading double underscore when name mangling is desired to avoid name collisions or prevent a sublclass from overwriting an attribute.

***Use a single underscore for 'private' attributes/methods and a double underscore for name mangling.***
