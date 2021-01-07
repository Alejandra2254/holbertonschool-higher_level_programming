# 0x07. Python - Test-driven development
Unit test save the day, doctest tests source code by running examples embedded in the documentation and verifying that they produce the expected results.

## General Objetives
1. What’s an interactive test?
Are snippets of text that are run to see if the program works exactly as shown. It is like giving examples that can be executed in the program with their respective expected output. These examples are extracted from expressions of document strings in class, module or function.

2. Why tests are important?
to be able to identify errors more quickly and correct them in the shortest possible time. Software testing helps reduce development risks, time and costs.

3. How to write Docstrings to create tests?

### Docstrings format

There are two options for writing a Doctest:
* They can be written in text fragments (in the same code)
* Another simple application of doctest is to test interactive examples in a text file. (Doctest in a different file)

Example:
```
def  mi_función ( a ,  b ): 
    "" " 
    >>> mi_función (2, 3) 
    6 
    >>> mi_función ('a', 3) 
    'aaa' 
    " "" 
    return  a  *  b
```
