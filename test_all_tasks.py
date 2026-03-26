#!/usr/bin/python3

print("=== Testing All 28 Tasks ===")

# Task 0: What function prints type of object?
print("Task 0: type")

# Task 1: What function gets variable identifier?
print("Task 1: id")

# Task 2: a = 89, b = 100, do they point to same object?
a = 89
b = 100
print(f"Task 2: {a is b}")

# Task 3: a = 89, b = 89, do they point to same object?
a = 89
b = 89
print(f"Task 3: {a is b}")

# Task 4: a = 89, b = a, do they point to same object?
a = 89
b = a
print(f"Task 4: {a is b}")

# Task 5: a = 89, b = a + 1, do they point to same object?
a = 89
b = a + 1
print(f"Task 5: {a is b}")

# Task 6: s1 = "Best School", s2 = s1, print(s1 == s2)
s1 = "Best School"
s2 = s1
print(f"Task 6: {s1 == s2}")

# Task 7: s1 = "Best", s2 = s1, print(s1 is s2)
s1 = "Best"
s2 = s1
print(f"Task 7: {s1 is s2}")

# Task 8: s1 = "Best School", s2 = "Best School", print(s1 == s2)
s1 = "Best School"
s2 = "Best School"
print(f"Task 8: {s1 == s2}")

# Task 9: s1 = "Best School", s2 = "Best School", print(s1 is s2)
s1 = "Best School"
s2 = "Best School"
print(f"Task 9: {s1 is s2}")

# Task 10: l1 = [1, 2, 3], l2 = [1, 2, 3], print(l1 == l2)
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(f"Task 10: {l1 == l2}")

# Task 11: l1 = [1, 2, 3], l2 = [1, 2, 3], print(l1 is l2)
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(f"Task 11: {l1 is l2}")

# Task 12: l1 = [1, 2, 3], l2 = l1, print(l1 == l2)
l1 = [1, 2, 3]
l2 = l1
print(f"Task 12: {l1 == l2}")

# Task 13: l1 = [1, 2, 3], l2 = l1, print(l1 is l2)
l1 = [1, 2, 3]
l2 = l1
print(f"Task 13: {l1 is l2}")

# Task 14: l1 = [1, 2, 3], l2 = l1, l1.append(4), print(l2)
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(f"Task 14: {l2}")

# Task 15: l1 = [1, 2, 3], l2 = l1, l1 = l1 + [4], print(l2)
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(f"Task 15: {l2}")

# Task 16: def increment(n): n += 1; a = 1; increment(a); print(a)
def increment(n):
    n += 1

a = 1
increment(a)
print(f"Task 16: {a}")

# Task 17: def increment(n): n.append(4); l = [1, 2, 3]; increment(l); print(l)
def increment_list(n):
    n.append(4)

l = [1, 2, 3]
increment_list(l)
print(f"Task 17: {l}")

# Task 18: def assign_value(n, v): n = v; l1 = [1, 2, 3]; l2 = [4, 5, 6]; assign_value(l1, l2); print(l1)
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(f"Task 18: {l1}")

# Task 20: a = (), is a a tuple?
a = ()
print(f"Task 20: {type(a) is tuple}")

# Task 21: a = (1, 2), is a a tuple?
a = (1, 2)
print(f"Task 21: {type(a) is tuple}")

# Task 22: a = (1), is a a tuple?
a = (1)
print(f"Task 22: {type(a) is tuple}")

# Task 23: a = (1, ), is a a tuple?
a = (1, )
print(f"Task 23: {type(a) is tuple}")

# Task 24: a = (1), b = (1), a is b
a = (1)
b = (1)
print(f"Task 24: {a is b}")

# Task 25: a = (1, 2), b = (1, 2), a is b
a = (1, 2)
b = (1, 2)
print(f"Task 25: {a is b}")

# Task 26: a = (), b = (), a is b
a = ()
b = ()
print(f"Task 26: {a is b}")

# Task 27: a = [1, 2, 3, 4], a = a + [5], will id(a) be same?
a = [1, 2, 3, 4]
id_before = id(a)
a = a + [5]
id_after = id(a)
print(f"Task 27: {id_before == id_after}")

# Task 28: a = [1, 2, 3], a += [4], will id(a) be same?
a = [1, 2, 3]
id_before = id(a)
a += [4]
id_after = id(a)
print(f"Task 28: {id_before == id_after}")