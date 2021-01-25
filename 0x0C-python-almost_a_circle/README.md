# 0x0C. Python - Almost a circle
## General Questions

### What is Unit testing and how to implement it in a large project
#### What is Unit Testing?
UNIT TESTING is a type of software testing where individual units or components of a software are tested. The purpose is to validate that each unit of the software code performs as expected. Unit Testing is done during the development (coding phase) of an application by the developers. Unit Tests isolate a section of code and verify its correctness. A unit may be an individual function, method, procedure, module, or object.

#### How to do Unit Testing
In order to do Unit Testing, developers write a section of code to test a specific function in software application. Developers can also isolate this function to test more rigorously which reveals unnecessary dependencies between function being tested and other units so the dependencies can be eliminated. Developers generally use UnitTest framework to develop automated test cases for unit testing.

1. create your function for example, volume_cuboid.py
```
def cuboid_volume(l):
    return (l*l*l)
```
2. Import the module
 ```
import unittest
```
3 The first function you will define is test_volume, which will check whether the output your cuboid_volume gives is equal to what you expect. To achieve this, you will make use of the assertAlmostEqual method.
```
class TestCuboid(unittest.TestCase):
def test_volume(self):
    self.assertAlmostEqual(cuboid_volume(2),8)
    self.assertAlmostEqual(cuboid_volume(1),1)
    self.assertAlmostEqual(cuboid_volume(0),0)
    self.assertAlmostEqual(cuboid_volume(5.5),166.375)
```
4. Let's run the above script. You would run the unittest module as a script by specifying -m while running it
```
!python -m unittest test_volume_cuboid.py
```
### How to serialize and deserialize a Class
### How to write and read a JSON file
### What is *args and how to use it
First of all let me tell you that it is not necessary to write *args or **kwargs. Only the * (aesteric) is necessary. You could have also written *var and **vars.
*args and **kwargs are mostly used in function definitions. *args and **kwargs allow you to pass a variable number of arguments to a function. What does variable mean here is that you do not know before hand that how many arguments can be passed to your function by the user so in this case you use these two keywords. *args is used to send a non-keyworded variable length argument list to the function. Here’s an example to help you get a clear idea:
```
def test_var_args(f_arg, *argv):
    print "first normal arg:", f_arg
    for arg in argv:
        print "another arg through *argv :", arg

test_var_args('yasoob','python','eggs','test')
```
This produces the following result:
```
first normal arg: yasoob
another arg through *argv : python
another arg through *argv : eggs
another arg through *argv : test
```
### What is **kwargs and how to use it
**kwargs allows you to pass keyworded variable length of arguments to a function. You should use **kwargs if you want to handle named arguments in a function. Here is an example to get you going with it:
```
def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.iteritems():
            print "%s == %s" %(key,value)
 
>>> greet_me(name="yasoob")
name == yasoob
```
### How to handle named arguments in a function
