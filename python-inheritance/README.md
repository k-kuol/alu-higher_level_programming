# Python - Inheritance

This project explores inheritance concepts in Python, including single inheritance, multiple inheritance, method overriding, and built-in functions related to inheritance.

## Learning Objectives

- Understanding superclass, baseclass, and parentclass concepts
- Understanding subclass concepts
- How to list all attributes and methods of a class or instance
- When an instance can have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- Understanding the default class every class inherits from
- How to override methods or attributes inherited from base class
- Which attributes or methods are available by heritage to subclasses
- Understanding the purpose of inheritance
- Using isinstance, issubclass, type and super built-in functions

## Files

### Python Scripts
- `0-lookup.py` - Function that returns list of available attributes and methods
- `1-my_list.py` - MyList class that inherits from list
- `2-is_same_class.py` - Function to check if object is exactly an instance of specified class
- `3-is_kind_of_class.py` - Function to check if object is instance of class or inherited class
- `4-inherits_from.py` - Function to check if object inherits from specified class
- `5-base_geometry.py` - Empty BaseGeometry class
- `6-base_geometry.py` - BaseGeometry class with area method
- `7-base_geometry.py` - BaseGeometry class with area and integer_validator methods
- `8-rectangle.py` - Rectangle class that inherits from BaseGeometry
- `9-rectangle.py` - Rectangle class with area method implementation
- `10-square.py` - Square class that inherits from Rectangle
- `11-square.py` - Square class that inherits from Rectangle (same as Rectangle behavior)

### Test Files
- `tests/1-my_list.txt` - Doctests for MyList class
- `tests/7-base_geometry.txt` - Doctests for BaseGeometry class

## Key Concepts

### Inheritance
- **Single Inheritance**: A class inherits from one parent class
- **Multiple Inheritance**: A class inherits from multiple parent classes
- **Method Resolution Order (MRO)**: The order in which methods are resolved in inheritance

### Built-in Functions
- `isinstance(obj, class)` - Check if object is instance of class
- `issubclass(class1, class2)` - Check if class1 is subclass of class2
- `type(obj)` - Get the exact type of object
- `super()` - Access methods from parent class

### Method Overriding
- Subclasses can override methods from parent classes
- Use `super()` to call parent class methods
- `__str__` and `__repr__` methods for string representation

## Requirements

- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files end with a new line
- First line of all files is exactly `#!/usr/bin/python3`
- Code uses pycodestyle (version 2.7.*)
- All files are executable
- All modules, classes, and functions have documentation
- All tests can be executed using: `python3 -m doctest ./tests/*`