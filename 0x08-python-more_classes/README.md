# Programing oriented to object 

Is another way of organizing your program which is to combine data and functionality and wrap it inside something called an object.
Used when writing large programs or have a problem that is better suited to this method, you can use object oriented programming techniques.

## Classes and Objects

Classes and objects are the two main aspects of object oriented programming. A class creates a new type where objects are instances of the class.
A class is created using the class keyword. The fields and methods of the class are listed in an indented block.

## Another Concepts 

* Fields: Variables that belong to an object or class are referred to as fields
  Fields are of two types - they can belong to each instance/object of the class or they can belong to the class itself. They are called instance variables and class variables respectively.
* Methods: Objects can also have functionality by using functions that belong to a class. Such functions are called methods of the class.
* Attributes: Collectively, the fields and methods can be referred to as the attributes of that class.

### The self

Class methods have only one specific difference from ordinary functions - they must have an extra first name that has to be added to the beginning of the parameter list, but you do not give a value for this parameter when you call the method, Python will provide it. This particular variable refers to the object itself, and by convention, it is given the name self.

### The __init__ method

The __init__ method is run as soon as an object of a class is instantiated (i.e. created). The method is useful to do any initialization (i.e. passing initial values to your object) you want to do with your object. 

## Class And Object Variables

### Class Variable 
are shared - they can be accessed by all instances of that class. There is only one copy of the class variable and when any one object makes a change to a class variable, that change will be seen by all the other instances.

### Object variables
are owned by each individual object/instance of the class. In this case, each object has its own copy of the field i.e. they are not shared and are not related in any way to the field by the same name in a different instance.
