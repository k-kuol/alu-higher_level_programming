# Python - Input/Output

This project covers file handling, JSON serialization/deserialization, and data manipulation in Python with optimized implementations.

## Learning Objectives

- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the with statement
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure

## Files

- `0-read_file.py` - Optimized function that reads a text file and prints it to stdout
- `1-write_file.py` - Function that writes a string to a text file
- `2-append_write.py` - Function that appends a string at the end of a text file
- `3-to_json_string.py` - Function that returns the JSON representation of an object
- `4-from_json_string.py` - Function that returns an object from a JSON string
- `5-save_to_json_file.py` - Function that writes an Object to a text file using JSON
- `6-load_from_json_file.py` - Optimized function that creates an Object from a JSON file
- `7-add_item.py` - Script that adds all arguments to a Python list and saves them to a file
- `8-class_to_json.py` - Function that returns dictionary description for JSON serialization
- `9-student.py` - Student class with to_json method
- `10-student.py` - Student class with filtered to_json method
- `11-student.py` - Student class with reload_from_json method
- `12-pascal_triangle.py` - Optimized function that returns Pascal's triangle
- `test_all.py` - Comprehensive test suite for all implementations

## Key Improvements

- **Code Optimization**: Removed redundant parameters and improved algorithm efficiency
- **Performance**: Enhanced Pascal's triangle algorithm for better performance
- **Consistency**: Standardized file opening patterns across all functions
- **Testing**: Added comprehensive test suite to verify all implementations
- **Documentation**: Enhanced docstrings and comments for better clarity

## Requirements

- All files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/python3`
- Code uses the pycodestyle (version 2.7.*)
- All files are executable
- All modules, classes and functions have documentation

## Usage

Run the test suite to verify all implementations:
```bash
python test_all.py
```