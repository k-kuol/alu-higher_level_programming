# Python - Everything is object

This project explores Python's object model and how Python handles different types of objects, focusing on the concepts of mutability, immutability, references, and aliases.

## Learning Objectives

- Understanding that everything in Python is an object
- Difference between mutable and immutable objects
- Understanding references and aliases
- How Python passes variables to functions
- Memory management and object identity
- The difference between `==` and `is` operators

## Files

### Answer Files (.txt)
- `0-answer.txt` to `28-answer.txt` - Answers to specific questions about Python object behavior

### Python Files
- `19-copy_list.py` - Function that returns a copy of a list

## Key Concepts

### Mutable vs Immutable Objects

**Immutable objects**: int, float, string, tuple, frozenset, bytes
- Cannot be changed after creation
- Operations create new objects

**Mutable objects**: list, dict, set, bytearray
- Can be modified in place
- Operations can modify the existing object

### Identity vs Equality
- `==` checks for equality (same value)
- `is` checks for identity (same object in memory)
- `id()` function returns the memory address of an object

### Function Arguments
- Python passes arguments by assignment
- For immutable objects: changes inside function don't affect original
- For mutable objects: modifications inside function affect the original object

## Requirements

- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files end with a new line
- Code uses pycodestyle (version 2.7.*)
- All files are executable