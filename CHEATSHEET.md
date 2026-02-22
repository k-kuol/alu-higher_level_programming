# Python Quick Reference Cheat Sheet

## String Indexing & Slicing

### Indexing (Single Character)
```python
text = "Python"
#       012345   (positive)
#      -654321   (negative)

text[0]    # 'P' (first)
text[5]    # 'n' (last)
text[-1]   # 'n' (last)
text[-2]   # 'o' (second to last)
```

### Slicing (Substring)
```python
text = "Python is cool"

text[0:6]    # "Python"  (index 0 to 5)
text[:6]     # "Python"  (start to 5)
text[7:]     # "is cool" (7 to end)
text[7:9]    # "is"      (7 to 8)
text[-4:]    # "cool"    (last 4)
text[:-5]    # "Python is" (all except last 5)
text[1:-1]   # "ython is coo" (without first & last)
```

**Remember:** `[start:end]` - end is NOT included!

---

## Print Function

### Basic Print
```python
print("Hello")                    # Hello
print("Hello", "World")           # Hello World
print("Hello", "World", sep="-")  # Hello-World
```

### Print Variables
```python
name = "Alice"
age = 25
print(name)                       # Alice
print(name, age)                  # Alice 25
```

### F-strings (Best Way!)
```python
name = "Bob"
age = 30
print(f"I'm {name}, {age} years old")  # I'm Bob, 30 years old

# With formatting
pi = 3.14159
print(f"Pi is {pi:.2f}")          # Pi is 3.14
```

---

## String Operations

### Concatenation
```python
"Hello" + " " + "World"           # "Hello World"
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2        # "Hello World"
```

### Repetition
```python
"Ha" * 3                          # "HaHaHa"
"=" * 10                          # "=========="
```

### Length
```python
len("Python")                     # 6
len("Hello World")                # 11
```

---

## Format Specifiers (F-strings)

```python
num = 3.14159
x = 42

f"{num:.2f}"      # "3.14"     (2 decimal places)
f"{num:.4f}"      # "3.1416"   (4 decimal places)
f"{x:05d}"        # "00042"    (pad with zeros, width 5)
f"{x:>5}"         # "   42"    (right align, width 5)
f"{x:<5}"         # "42   "    (left align, width 5)
```

---

## Escape Sequences

```python
print("\"")       # "  (double quote)
print("\'")       # '  (single quote)
print("\\")       # \  (backslash)
print("\n")       # (newline)
print("\t")       # (tab)
```

---

## Python Interpreter

### Interactive Mode
```bash
python3
>>> print("Hello")
Hello
>>> 2 + 2
4
>>> exit()
```

### Run Python File
```bash
python3 script.py
```

### Run Python Code Inline
```bash
python3 -c 'print("Hello")'
```

### Run with Environment Variable
```bash
export PYFILE=script.py
python3 $PYFILE
```

---

## Common Mistakes to Avoid

### ❌ Wrong
```python
text = "Python"
print(text[6])        # IndexError! (no index 6)
print(text[1:1])      # "" (empty - start equals end)
```

### ✅ Correct
```python
text = "Python"
print(text[5])        # "n" (last character)
print(text[-1])       # "n" (last character)
print(text[1:3])      # "yt" (indices 1 and 2)
```

---

## Pycodestyle Tips

### Good Style ✅
```python
x = 5                 # spaces around =
y = x + 10            # spaces around +
name = "Alice"        # descriptive names

def my_function():    # lowercase with underscores
    pass
```

### Bad Style ❌
```python
x=5                   # no spaces
y=x+10                # no spaces
a = "Alice"           # unclear name

def MyFunction():     # should be lowercase
    pass
```

### Check Your Code
```bash
pycodestyle script.py
```

---

## Quick Tips

1. **Indexing starts at 0** - First character is index 0
2. **Negative indices** - Count from the end (-1 is last)
3. **Slicing end is exclusive** - `[0:3]` gives indices 0, 1, 2 (not 3)
4. **F-strings are modern** - Use `f"{var}"` instead of `"{}".format(var)`
5. **Strings are immutable** - Can't change individual characters
6. **Use pycodestyle** - Keep your code clean and readable

---

## The Zen of Python (Key Points)

```python
import this  # Run this to see all 19 principles
```

Most important ones:
- Beautiful is better than ugly
- Simple is better than complex
- Readability counts
- There should be one obvious way to do it

---

## File Requirements Checklist

### Python Scripts (.py)
- [ ] First line: `#!/usr/bin/python3`
- [ ] File ends with newline
- [ ] File is executable: `chmod +x file.py`
- [ ] Passes pycodestyle: `pycodestyle file.py`
- [ ] Code is 3-5 lines (as specified in task)

### Shell Scripts
- [ ] First line: `#!/bin/bash`
- [ ] Exactly 2 lines long: `wc -l file`
- [ ] File ends with newline
- [ ] File is executable: `chmod +x file`

### Make File Executable
```bash
chmod +x filename
```

### Check Line Count
```bash
wc -l filename
```
