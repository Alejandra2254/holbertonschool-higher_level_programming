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
### What about Exceptions?
No problem, provided that the traceback is the only output produced by the example: just paste in the traceback. Since tracebacks contain details that are likely to change rapidly (for example, exact file paths and line numbers), this is one case where doctest works hard to be flexible in what it accepts.
```
>>> [1, 2, 3].remove(42)
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
ValueError: list.remove(x): x not in list
```
The expected output for an exception must start with a traceback header, which may be either of the following two lines, indented the same as the first line of the example:
```
Traceback (most recent call last):
Traceback (innermost last):
```
Best practice is to omit the traceback stack, unless it adds significant documentation value to the example. So the last example is probably better as:
```
>>> raise ValueError('multi\n    line\ndetail')
Traceback (most recent call last):
    ...
ValueError: multi
    line
detail
```
4. How to write documentation for each module and function?
All of the tests in the examples so far have been written in the docstrings of the functions they are testing. That is convenient for users who examine the docstrings for help using the function (especially with pydoc), but doctest looks for tests in other places, too. The obvious location for additional tests is in the docstrings elsewhere in the module.
```
#doctest_docstrings.py
"""Tests can appear in any docstring within the module.

Module-level tests cross class and function boundaries.

>>> A('a') == B('b')
False
"""


class A:
    """Simple class.

    >>> A('instance_name').name
    'instance_name'
    """

    def __init__(self, name):
        self.name = name

    def method(self):
        """Returns an unusual value.

        >>> A('name').method()
        'eman'
        """
        return ''.join(reversed(self.name))


class B(A):
    """Another simple class.

    >>> B('different_name').name
    'different_name'
    """
```
Docstrings at the module, class, and function levels can all contain tests.

```
 $python3 -m doctest -v doctest_docstrings.py

Trying:
    A('a') == B('b')
Expecting:
    False
ok
Trying:
    A('instance_name').name
Expecting:
    'instance_name'
ok
Trying:
    A('name').method()
Expecting:
    'eman'
ok
Trying:
    B('different_name').name
Expecting:
    'different_name'
ok
1 items had no tests:
    doctest_docstrings.A.__init__
4 items passed all tests:
   1 tests in doctest_docstrings
   1 tests in doctest_docstrings.A
   1 tests in doctest_docstrings.A.method
   1 tests in doctest_docstrings.B
4 tests in 5 items.
4 passed and 0 failed.
Test passed.
```
