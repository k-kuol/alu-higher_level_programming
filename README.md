# Python - Hello, World

## Why Python Programming is Awesome

Python is awesome because:
- **Easy to Learn**: Simple, readable syntax that looks like English
- **Versatile**: Used for web development, data science, AI, automation, and more
- **Huge Community**: Millions of developers and tons of libraries
- **Cross-Platform**: Works on Windows, Mac, Linux
- **High Demand**: One of the most sought-after programming languages in jobs

## Who Created Python?

**Guido van Rossum** created Python in the late 1980s and released it in 1991.

## Who is Guido van Rossum?

Guido van Rossum is a Dutch programmer who:
- Created Python while working at CWI in the Netherlands
- Was Python's "Benevolent Dictator For Life" (BDFL) until 2018
- Now works at Microsoft (as of 2020)
- Designed Python to be fun and easy to use

## Where Does the Name 'Python' Come From?

The name "Python" comes from **"Monty Python's Flying Circus"**, a British comedy show that Guido van Rossum enjoyed. It has nothing to do with the snake!

## What is the Zen of Python?

The Zen of Python is a collection of 19 guiding principles for writing Python code. You can see it by typing `import this` in Python. Key principles include:
- Beautiful is better than ugly
- Simple is better than complex
- Readability counts

## How to Use the Python Interpreter

### Interactive Mode:
```bash
python3
>>> print("Hello")
Hello
>>> exit()
```

### Run a Python File:
```bash
python3 script.py
```

### Run Python Code Inline:
```bash
python3 -c 'print("Hello")'
```

## How to Print Text and Variables Using Print

### Basic Printing:
```python
print("Hello, World!")  # Prints text
```

### Printing Variables:
```python
name = "Alice"
age = 25
print(name)  # Prints: Alice
print(age)   # Prints: 25
```

### Using F-strings (Modern Way):
```python
name = "Bob"
age = 30
print(f"My name is {name} and I'm {age} years old")
# Prints: My name is Bob and I'm 30 years old
```

### Printing Multiple Items:
```python
print("Hello", "World", 123)  # Prints: Hello World 123
```

## How to Use Strings

### Creating Strings:
```python
str1 = "Hello"
str2 = 'World'
str3 = """Multi
line
string"""
```

### String Operations:
```python
# Concatenation
greeting = "Hello" + " " + "World"  # "Hello World"

# Repetition
laugh = "Ha" * 3  # "HaHaHa"

# Length
length = len("Python")  # 6
```

## What are Indexing and Slicing in Python?

### Indexing (Getting Single Characters):
```python
text = "Python"
#       012345  (positive indexing)
#      -654321  (negative indexing)

print(text[0])   # P (first character)
print(text[5])   # n (last character)
print(text[-1])  # n (last character using negative index)
print(text[-2])  # o (second to last)
```

### Slicing (Getting Substrings):
```python
text = "Python is cool"

# Syntax: string[start:end]  (end is NOT included)
print(text[0:6])   # "Python" (from index 0 to 5)
print(text[:6])    # "Python" (from beginning to 5)
print(text[7:])    # "is cool" (from index 7 to end)
print(text[7:9])   # "is" (from index 7 to 8)
print(text[:-5])   # "Python is" (from start to 5 from end)
print(text[-4:])   # "cool" (last 4 characters)
```

**Key Points:**
- Indexing starts at 0
- Negative indices count from the end (-1 is last)
- Slicing: `[start:end]` - end is NOT included
- `[:n]` means "from beginning to n"
- `[n:]` means "from n to end"

## What is the Official Python Coding Style?

The official style guide is **PEP 8**. Key rules:
- Use 4 spaces for indentation (not tabs)
- Lines should be max 79 characters
- Use lowercase with underscores for variable names: `my_variable`
- Use blank lines to separate functions
- Add spaces around operators: `x = 5` not `x=5`

### How to Check Your Code with pycodestyle:

Install:
```bash
pip install pycodestyle
```

Check a file:
```bash
pycodestyle script.py
```

Check all Python files:
```bash
pycodestyle *.py
```

## Requirements

### Python Scripts:
- Allowed editors: vi, vim, emacs
- Files interpreted on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- First line: `#!/usr/bin/python3`
- Code should use pycodestyle (version 2.7.*)
- All files must be executable
- README.md file is mandatory

### Shell Scripts:
- Allowed editors: vi, vim, emacs
- Tested on Ubuntu 20.04 LTS
- Scripts should be exactly two lines long
- All files should end with a new line
- First line: `#!/bin/bash`
- All files must be executable

## Project Tasks

This project contains the following tasks:
- 0-run: Shell script that runs a Python script
- 1-run_inline: Shell script that runs Python code inline
- 2-print.py: Print a specific string
- 3-print_number.py: Print integer with f-strings
- 4-print_float.py: Print float with precision
- 5-print_string.py: Print string multiple times and slice it
- 6-concat.py: Concatenate strings
- 7-edges.py: String slicing practice
- 8-concat_edges.py: Advanced string manipulation
- 9-easter_egg.py: Print the Zen of Python

## Repository

- GitHub repository: alu-higher_level_programming
- Directory: python-hello_world
