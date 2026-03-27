#!/usr/bin/python3
"""Test script for all Python I/O functions"""

# Test imports
from importlib import import_module
import json
import os

def test_all_functions():
    """Test all implemented functions"""
    print("Testing Python I/O Project...")
    
    # Test 0-read_file
    print("\n1. Testing read_file...")
    read_file = import_module('0-read_file').read_file
    with open('test.txt', 'w') as f:
        f.write('Hello World!')
    read_file('test.txt')
    
    # Test 1-write_file
    print("\n2. Testing write_file...")
    write_file = import_module('1-write_file').write_file
    chars = write_file('output.txt', 'Python is awesome!')
    print(f"Characters written: {chars}")
    
    # Test 2-append_write
    print("\n3. Testing append_write...")
    append_write = import_module('2-append_write').append_write
    chars = append_write('output.txt', '\nAppended text!')
    print(f"Characters appended: {chars}")
    
    # Test 3-to_json_string
    print("\n4. Testing to_json_string...")
    to_json_string = import_module('3-to_json_string').to_json_string
    data = {'name': 'John', 'age': 30}
    json_str = to_json_string(data)
    print(f"JSON string: {json_str}")
    
    # Test 4-from_json_string
    print("\n5. Testing from_json_string...")
    from_json_string = import_module('4-from_json_string').from_json_string
    obj = from_json_string(json_str)
    print(f"Object: {obj}")
    
    # Test 9-student
    print("\n6. Testing Student class...")
    Student = import_module('9-student').Student
    student = Student('John', 'Doe', 25)
    print(f"Student JSON: {student.to_json()}")
    
    # Test 12-pascal_triangle
    print("\n7. Testing Pascal's triangle...")
    pascal_triangle = import_module('12-pascal_triangle').pascal_triangle
    triangle = pascal_triangle(5)
    for row in triangle:
        print(row)
    
    # Cleanup
    if os.path.exists('test.txt'):
        os.remove('test.txt')
    if os.path.exists('output.txt'):
        os.remove('output.txt')
    
    print("\nAll tests completed successfully!")

if __name__ == "__main__":
    test_all_functions()