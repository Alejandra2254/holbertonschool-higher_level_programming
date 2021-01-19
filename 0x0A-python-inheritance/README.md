# 0x0A. Python - Inheritance

Inheritance is one of the premises and techniques of OOP which allows programmers to create a general class first and then later to create more specialized classes that reuse code from the general class. Inheritance also allows you to write cleaner and more readable code.

## General Questions

### What is a superclass, baseclass or parentclass

A class that is derived from another class is called a subclass (also a derived class, extended class, or child class). The class from which the subclass is derived is called a superclass (also a base class or a parent class).

### What is a subclass

A subclass is a class that derives from another class. A subclass inherits state and behavior from all of its ancestors. The term superclass refers to a class's direct ancestor as well as all of its ascendant classes.

###How to list all attributes and methods of a class or instance

Using __dict__ attribute.
__dict__ attribute that instances of the class. It is an object descriptor that returns the internal dictionary of the attributes of the specific instance. In summary, the __dict__ attribute of an object cannot be stored in the object of the __dict__, so it is accessed through a descriptor defined in the class.

### When can an instance have new attributes

nstance attributes are owned by the specific instances of a class. That is, for two different instances, the instance attributes are usually different. You should by now be familiar with this concept which we introduced in our previous chapter.

We can also define attributes at the class level. Class attributes are attributes which are owned by the class itself. They will be shared by all the instances of the class. Therefore they have the same value for every instance. We define class attributes outside all the methods, usually they are placed at the top, right below the class header

### How to inherit class from another

```python
class Person:
  def __init__(self, fname, lname):
      self.firstname = fname
          self.lastname = lname

  def printname(self):
      print(self.firstname, self.lastname)
      #Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
```

Create a class named Student, which will inherit the properties and methods from the Person class:
```python
class Student(Person):
  pass
```
### How to define a class with multiple base classes

Unlike languages like Java and C #, the Python language allows multiple inheritance, that is, it can inherit from multiple classes.
Multiple inheritance is the ability of a subclass to inherit from multiple super classes.
This leads to a problem, and that is that if several super classes have the same attributes or methods, the subclass can only inherit from one of them.
In these cases Python will give priority to the leftmost classes at the time of the subclass declaration:

What is the default class every class inherit from
How to override a method or attribute inherited from the base class
Which attributes or methods are available by heritage to subclasses
What is the purpose of inheritance
What are, when and how to use isinstance, issubclass, type and super built-in functions