# 0x0B. Python - Input/Output

### How to open a file

The open() function opens a file, and returns it as a file object.
```open(file, mode)```
where
* file	The path and name of the file
* mode	A string, define which mode you want to open the file in:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exist

### How to write text in a file
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content

### How to read the full content of a file

The read() method returns the specified number of bytes from the file. Default is -1 which means the whole file.
```file.read()```
* size	Optional. The number of bytes to return. Default -1, which means the whole file.
How to read a file line by line
How to move the cursor in a file
How to make sure a file is closed after using it
### What is and how to use the with statement
with statement in Python is used in exception handling to make the code cleaner and much more readable. It simplifies the management of common resources like file streams. Observe the following code example on how the use of with statement makes code cleaner.
```
# file handling 
  
# 1) without using with statement 
file = open('file_path', 'w') 
file.write('hello world !') 
file.close() 
  
# 2) without using with statement 
file = open('file_path', 'w') 
try: 
    file.write('hello world') 
finally: 
    file.close() 
```
 
```
filter_none
brightness_4
# using with statement 
with open('file_path', 'w') as file: 
    file.write('hello world !') 
```
### What is JSON
 JSON (JavaScript Object Notation),
 * JSON is a syntax for storing and exchanging data.
 * JSON is text, written with JavaScript object notation.
 Python has a built-in package called json, which can be used to work with JSON data.
 
 Strings can easily be written to and read from a file. Numbers take a bit more effort, since the read() method only returns strings, which will have to be passed to a function like int(), which takes a string like '123' and returns its numeric value 123. When you want to save more complex data types like nested lists and dictionaries, parsing and serializing by hand becomes complicated.
 
What is serialization
What is deserialization
### How to convert a Python data structure to a JSON string
```
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
```
### How to convert a JSON string to a Python data structure
```
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
```
