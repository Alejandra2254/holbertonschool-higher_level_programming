# 0x13. JavaScript - Objects, Scopes and Closures

GENERAL

### Why JavaScript programming is amazing

For now, let’s simply say that JavaScript is a tool for developers to add interactivity to websites.
*Everything that can be written in javascript will be written in javascript*

### How to create an object in JavaScript

As with many things in JavaScript, creating an object often begins with defining and initializing a variable. Try entering the following line below the JavaScript code that's already in your file, then saving and refreshing:

```
const person = {};
```
Congratulations, you've just created your first object. Job done! But this is an empty object, so we can't really do much with it. Let's update the JavaScript object in our file to look like this:
```
const person = {
  name: ['Bob', 'Smith'],
    age: 32,
      gender: 'male',
        interests: ['music', 'skiing'],
	  bio: function() {
	      alert(this.name[0] + ' ' + this.name[1] + ' is ' + this.age + ' years old. He likes ' + this.interests[0] + ' and ' + this.interests[1] + '.');
},
  greeting: function() {
      alert('Hi! I\'m ' + this.name[0] + '.');       
}
};
```

### What this means

The keyword refers to the current object the code is being written inside — so in this case is equivalent to .  it always ensures that the correct values are used when a member's context changes (for example, two different object instances may have different names, but we want to use their own name when saying their greeting).

Let's illustrate what we mean with a simplified pair of person objects:
```
const person1 = {
  name: 'Chris',
    greeting: function() {
        alert('Hi! I\'m ' + this.name + '.');
	  
}

}

const person2 = {
  name: 'Deepti',
    greeting: function() {
        alert('Hi! I\'m ' + this.name + '.');
	  
}
}
```

### What undefined means

undefined is a property of the global object. That is, it is a variable in global scope. The initial value of undefined is the primitive value undefined.

### Why the variable type and scope is important

### What is a closure

A closure is the combination of a function bundled together (enclosed) with references to its surrounding state (the lexical environment). In other words, a closure gives you access to an outer function’s scope from an inner function. In JavaScript, closures are created every time a function is created, at function creation time.

### What is a prototype

Prototypes are the mechanism by which JavaScript objects inherit features from one another. In this article, we explain how prototype chains work and look at how the prototype property can be used to add methods to existing constructors.

### How to inherit an object from another

To create a subclass we use the extends keyword to tell JavaScript the class we want to base our class on

```
class Teacher extends Person {
  constructor(subject, grade) {
      this.subject = subject;
          this.grade = grade;	    
}
}
```