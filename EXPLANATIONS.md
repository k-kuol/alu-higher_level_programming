# Task Explanations - Python Hello World

## Task 0: Run Python File (0-run)

**What it does:** Runs a Python script whose filename is stored in an environment variable.

**Explanation:**
```bash
#!/bin/bash
python3 $PYFILE
```
- `#!/bin/bash` - Shebang that tells the system to use bash shell
- `python3` - The Python 3 interpreter
- `$PYFILE` - Environment variable containing the Python filename

**How to use:**
```bash
export PYFILE=main.py
./0-run
```

---

## Task 1: Run Inline (1-run_inline)

**What it does:** Runs Python code directly from an environment variable.

**Explanation:**
```bash
#!/bin/bash
python3 -c "$PYCODE"
```
- `python3 -c` - Runs Python code from command line
- `"$PYCODE"` - Environment variable containing Python code (quotes preserve spaces)

**How to use:**
```bash
export PYCODE='print("Hello")'
./1-run_inline
```

---

## Task 2: Hello, Print (2-print.py)

**What it does:** Prints a string with a double quote at the beginning.

**Explanation:**
```python
#!/usr/bin/python3
print("\"Programming is like building a multilingual puzzle")
```
- `#!/usr/bin/python3` - Shebang for Python 3
- `\"` - Escape sequence to print a double quote character
- The backslash `\` tells Python "treat the next character as literal text, not code"

**Output:** `"Programming is like building a multilingual puzzle`

---

## Task 3: Print Integer (3-print_number.py)

**What it does:** Prints an integer using f-strings.

**Explanation:**
```python
#!/usr/bin/python3
number = 98
print(f"{number} Battery street")
```
- `f"{number}"` - F-string (formatted string literal)
- `{number}` - Placeholder that gets replaced with the variable's value
- No need to convert int to string - f-strings do it automatically

**Output:** `98 Battery street`

---

## Task 4: Print Float (4-print_float.py)

**What it does:** Prints a float with exactly 2 decimal places.

**Explanation:**
```python
#!/usr/bin/python3
number = 3.14159
print(f"Float: {number:.2f}")
```
- `{number:.2f}` - Format specifier
  - `:` - Start of format specification
  - `.2` - Show 2 digits after decimal point
  - `f` - Format as float
- Automatically rounds the number (3.14159 → 3.14)

**Output:** `Float: 3.14`

---

## Task 5: Print String (5-print_string.py)

**What it does:** Prints a string 3 times, then prints its first 9 characters.

**Explanation:**
```python
#!/usr/bin/python3
str = "Holberton School"
print(str * 3)
print(str[:9])
```
- `str * 3` - String repetition (multiplies the string)
- `str[:9]` - Slice from beginning to index 9 (not included)
  - Characters 0-8: "Holberton"

**Output:**
```
Holberton SchoolHolberton SchoolHolberton School
Holberton
```

---

## Task 6: Play with Strings (6-concat.py)

**What it does:** Concatenates two strings to create a welcome message.

**Explanation:**
```python
#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
str1 = str1 + " " + str2
print(f"Welcome to {str1}!")
```
- `str1 + " " + str2` - String concatenation
  - Joins "Holberton" + " " + "School" = "Holberton School"
- `str1 = ...` - Updates str1 with the new value
- `f"Welcome to {str1}!"` - Embeds the concatenated string

**Output:** `Welcome to Holberton School!`

---

## Task 7: Copy - Cut - Paste (7-edges.py)

**What it does:** Demonstrates string slicing to extract parts of a string.

**Explanation:**
```python
#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
```

**Breaking it down:**
- `word[:3]` - First 3 characters
  - From start to index 3 (not included): "Hol"
  
- `word[-2:]` - Last 2 characters
  - From 2nd-to-last to end: "on"
  
- `word[1:-1]` - Middle (without first and last)
  - From index 1 to 1-from-end: "olberto"

**Visual representation:**
```
word = "Holberton"
Index:  012345678
       -987654321

[:3]   = "Hol"      (indices 0,1,2)
[-2:]  = "on"       (indices 7,8)
[1:-1] = "olberto"  (indices 1,2,3,4,5,6,7)
```

**Output:**
```
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
```

---

## Task 8: Create a New Sentence (8-concat_edges.py)

**What it does:** Extracts and combines specific parts of a string to form a new sentence.

**Explanation:**
```python
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[39:67] + str[107:112] + str[:6]
print(str)
```

**Breaking it down:**
Original string positions:
- `str[39:67]` = "object-oriented programming"
- `str[107:112]` = " with"
- `str[:6]` = "Python"

Combined: "object-oriented programming" + " with" + " Python"

**Output:** `object-oriented programming with Python`

**Why this works:**
- We're slicing specific indices that contain the words we need
- Concatenating them in the right order creates our target sentence
- No new variables or string literals allowed - only slicing!

---

## Task 9: Easter Egg (9-easter_egg.py)

**What it does:** Prints the Zen of Python.

**Explanation:**
```python
#!/usr/bin/python3
import this
```
- `import this` - Special Python module
- When imported, it automatically prints the Zen of Python
- It's an "Easter egg" (hidden feature) in Python
- The module contains the 19 guiding principles for Python code

**Output:** The complete Zen of Python (19 aphorisms)

---

## Key Concepts Summary

### 1. String Indexing
- Positive: `str[0]` is first character
- Negative: `str[-1]` is last character

### 2. String Slicing
- `str[start:end]` - from start to end (end not included)
- `str[:n]` - from beginning to n
- `str[n:]` - from n to end
- `str[start:end]` - from start to end

### 3. F-strings
- `f"text {variable}"` - embed variables in strings
- `f"{num:.2f}"` - format numbers (2 decimal places)

### 4. String Operations
- `str * 3` - repeat string 3 times
- `str1 + str2` - concatenate strings

### 5. Escape Sequences
- `\"` - double quote
- `\'` - single quote
- `\\` - backslash
- `\n` - newline

### 6. Shell Scripts
- Must be exactly 2 lines
- First line: `#!/bin/bash`
- Use `$VARIABLE` to access environment variables
- `python3 -c "code"` runs Python code inline
