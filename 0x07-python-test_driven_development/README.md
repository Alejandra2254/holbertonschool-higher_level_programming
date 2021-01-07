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
To run the tests, use doctest as the main program using the -m option of the interpreter. Generally, no results are produced while the tests are running, so the following example includes the -v option to make the result more verbose.

```
$ python -m doctest -v doctest_simple.py

Trying:
    my_function(2, 3)
Expecting:
    6
ok
Trying:
    my_function('a', 3)
Expecting:
    'aaa'
ok
1 items had no tests:
    doctest_simple
1 items passed all tests:
   2 tests in doctest_simple.my_function
2 tests in 2 items.
2 passed and 0 failed.
Test passed.
```
