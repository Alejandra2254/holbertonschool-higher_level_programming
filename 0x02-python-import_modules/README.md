# Import modules in Phyton

## Module
A module allows you to logically organize your Python code. Grouping related code into a module makes the code easier to understand and use. A module is a Python object with arbitrarily named attributes that you can bind and reference.

Simply, a module is a file consisting of Python code. A module can define functions, classes and variables. A module can also include runnable code.

## Example
The Python code for a module named aname normally resides in a file named aname.py. Here's an example of a simple module, support.py

    def print_func( par ):
   print "Hello : ", par
   return`

## The import Statement
You can use any Python source file as a module by executing an import statement in some other Python source file. The import has the following syntax −
import module1[, module2[,... moduleN]