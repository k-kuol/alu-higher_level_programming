# Visual Learning Guide - Python Strings

## Understanding String Indexing

### Example 1: "Python"
```
String: P  y  t  h  o  n
Index:  0  1  2  3  4  5    (positive indexing)
       -6 -5 -4 -3 -2 -1    (negative indexing)
```

**Examples:**
- `"Python"[0]` → `P` (first character)
- `"Python"[3]` → `h` (fourth character)
- `"Python"[-1]` → `n` (last character)
- `"Python"[-3]` → `h` (third from end)

---

## Understanding String Slicing

### The Rule: `string[start:end]`
- **start**: included (where to begin)
- **end**: NOT included (where to stop)

### Example 2: "Python is cool"
```
String: P  y  t  h  o  n     i  s     c  o  o  l
Index:  0  1  2  3  4  5  6  7  8  9 10 11 12 13
       -14-13-12-11-10-9 -8 -7 -6 -5 -4 -3 -2 -1
```

**Slicing Examples:**

1. `"Python is cool"[0:6]` → `"Python"`
   ```
   Start at 0 (P), stop before 6 (space)
   P  y  t  h  o  n
   0  1  2  3  4  5  [6]
   ✓  ✓  ✓  ✓  ✓  ✓   ✗
   ```

2. `"Python is cool"[7:9]` → `"is"`
   ```
   Start at 7 (i), stop before 9 (space)
      i  s
      7  8  [9]
      ✓  ✓   ✗
   ```

3. `"Python is cool"[7:]` → `"is cool"`
   ```
   Start at 7 (i), go to end
      i  s     c  o  o  l
      7  8  9 10 11 12 13
      ✓  ✓  ✓  ✓  ✓  ✓  ✓
   ```

4. `"Python is cool"[:6]` → `"Python"`
   ```
   Start at beginning, stop before 6
   P  y  t  h  o  n
   0  1  2  3  4  5  [6]
   ✓  ✓  ✓  ✓  ✓  ✓   ✗
   ```

5. `"Python is cool"[-4:]` → `"cool"`
   ```
   Start at -4 (c), go to end
         c  o  o  l
        -4 -3 -2 -1
         ✓  ✓  ✓  ✓
   ```

6. `"Python is cool"[:-5]` → `"Python is"`
   ```
   Start at beginning, stop before -5 (space before 'c')
   P  y  t  h  o  n     i  s  [-5]
   0  1  2  3  4  5  6  7  8   9
   ✓  ✓  ✓  ✓  ✓  ✓  ✓  ✓  ✓   ✗
   ```

---

## Example 3: "Holberton"

```
String: H  o  l  b  e  r  t  o  n
Index:  0  1  2  3  4  5  6  7  8
       -9 -8 -7 -6 -5 -4 -3 -2 -1
```

### Task 7 Breakdown:

**1. First 3 letters: `word[:3]`**
```
H  o  l  [3]
0  1  2   ✗
✓  ✓  ✓
Result: "Hol"
```

**2. Last 2 letters: `word[-2:]`**
```
      o  n
     -2 -1
      ✓  ✓
Result: "on"
```

**3. Middle word: `word[1:-1]`**
```
[0] o  l  b  e  r  t  o  [-1]
 ✗  1  2  3  4  5  6  7   ✗
    ✓  ✓  ✓  ✓  ✓  ✓  ✓
Result: "olberto"
```

---

## F-string Formatting Examples

### Basic F-strings
```python
name = "Alice"
age = 25

# Simple variable insertion
f"Hello, {name}"                    # "Hello, Alice"
f"{name} is {age} years old"        # "Alice is 25 years old"

# Expressions inside {}
f"Next year: {age + 1}"             # "Next year: 26"
f"Double: {age * 2}"                # "Double: 50"
```

### Number Formatting
```python
pi = 3.14159265359

f"{pi}"           # "3.14159265359"  (default)
f"{pi:.2f}"       # "3.14"           (2 decimals)
f"{pi:.4f}"       # "3.1416"         (4 decimals, rounded)
f"{pi:.0f}"       # "3"              (no decimals)
```

### Visual Breakdown of `{pi:.2f}`
```
{  pi  :  .2  f  }
│  │   │  │   │  │
│  │   │  │   │  └─ Format as float
│  │   │  │   └──── 2 digits after decimal
│  │   │  └──────── Start format specification
│  │   └─────────── Variable name
│  └─────────────── Opening brace
└────────────────── Closing brace
```

---

## String Operations Visual Guide

### Concatenation (+)
```python
"Hello" + " " + "World"

  "Hello"  +  " "  +  "World"
     ↓         ↓        ↓
  ─────────────────────────
           ↓
    "Hello World"
```

### Repetition (*)
```python
"Ha" * 3

  "Ha"  ×  3
    ↓      ↓
  ──────────
      ↓
  "HaHaHa"
```

### Multiple Operations
```python
("Hi" + " ") * 2

Step 1: "Hi" + " "  →  "Hi "
Step 2: "Hi " * 2   →  "Hi Hi "
```

---

## Common Patterns

### Get First N Characters
```python
text = "Python"
text[:3]    # "Pyt" (first 3)
text[:1]    # "P"   (first 1)
```

### Get Last N Characters
```python
text = "Python"
text[-3:]   # "hon" (last 3)
text[-1:]   # "n"   (last 1)
```

### Remove First N Characters
```python
text = "Python"
text[3:]    # "hon" (skip first 3)
text[1:]    # "ython" (skip first 1)
```

### Remove Last N Characters
```python
text = "Python"
text[:-3]   # "Pyt" (remove last 3)
text[:-1]   # "Pytho" (remove last 1)
```

### Get Middle (Remove First and Last)
```python
text = "Python"
text[1:-1]  # "ytho" (without first and last)
```

---

## Practice Exercises

### Exercise 1: "Hello World"
```
String: H  e  l  l  o     W  o  r  l  d
Index:  0  1  2  3  4  5  6  7  8  9 10
```

What do these return?
1. `"Hello World"[0]` → ?
2. `"Hello World"[6]` → ?
3. `"Hello World"[:5]` → ?
4. `"Hello World"[6:]` → ?
5. `"Hello World"[-5:]` → ?

**Answers:**
1. `H`
2. `W`
3. `Hello`
4. `World`
5. `World`

---

### Exercise 2: "Python is cool"
```
String: P  y  t  h  o  n     i  s     c  o  o  l
Index:  0  1  2  3  4  5  6  7  8  9 10 11 12 13
```

What do these return?
1. `"Python is cool"[7:-5]` → ?
2. `"Python is cool"[4]` → ?
3. `"Python is cool"[-2]` → ?
4. `"Python is cool"[0:6]` → ?
5. `"Python is cool"[7:]` → ?

**Answers:**
1. `is` (from 7 to before -5)
2. `o` (index 4)
3. `o` (second to last)
4. `Python` (first 6)
5. `is cool` (from 7 to end)

---

## Memory Tricks

### Remember Slicing
**"Start is IN, End is OUT"**
- The start index IS included
- The end index is NOT included

### Remember Negative Indexing
**"Count backwards from -1"**
- -1 is the last character
- -2 is second to last
- And so on...

### Remember F-strings
**"F for Format"**
- Put `f` before the string
- Put variables in `{curly braces}`
- Add `:` for special formatting

---

## Quick Reference Table

| Operation | Syntax | Example | Result |
|-----------|--------|---------|--------|
| Get character | `str[i]` | `"Python"[0]` | `"P"` |
| First N chars | `str[:n]` | `"Python"[:3]` | `"Pyt"` |
| Last N chars | `str[-n:]` | `"Python"[-3:]` | `"hon"` |
| From index to end | `str[n:]` | `"Python"[2:]` | `"thon"` |
| Up to index | `str[:n]` | `"Python"[:4]` | `"Pyth"` |
| Range | `str[a:b]` | `"Python"[1:4]` | `"yth"` |
| Concatenate | `str1 + str2` | `"Hi" + "!"` | `"Hi!"` |
| Repeat | `str * n` | `"Ha" * 3` | `"HaHaHa"` |
| Length | `len(str)` | `len("Hi")` | `2` |
| F-string | `f"{var}"` | `f"{5}"` | `"5"` |

---

## Tips for Success

1. **Practice with pen and paper** - Draw out the indices
2. **Remember: end is NOT included** - Most common mistake
3. **Use negative indices for "from the end"** - Very useful
4. **F-strings are your friend** - Modern and clean
5. **Test in Python interpreter** - Try examples yourself

```bash
python3
>>> "Python"[0:3]
'Pyt'
>>> "Python"[-3:]
'hon'
```
