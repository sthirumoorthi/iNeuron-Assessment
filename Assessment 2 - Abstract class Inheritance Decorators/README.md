# Abstract class, Multiple inheritance and Decorators in Python

## <u> Problem Statement:

Demonstrate use of abstract class, multiple inheritance and decorator in python using examples.
  
  
## Abstract Class:
  
Abstraction is implemented using the abstract classes. An abstract class in Python is typically created to declare a set of methods that must be created in any child class built on top of this abstract class. Similarly, an abstract method is one that doesn't have any implementation. An abstract base class is a class that is used as a blueprint for other classes.

![image](https://user-images.githubusercontent.com/90926526/172479154-98e35e1a-1806-497c-a036-5f876c6da04c.png)

### Output:
  
![image](https://user-images.githubusercontent.com/90926526/172479388-8f570e17-895b-4cdd-bcfa-f01b465123f4.png)

![image](https://user-images.githubusercontent.com/90926526/172482534-8f225211-aebe-4a89-88d9-12b819957af4.png)

  
## Multiple Inheritance:
  
Inheritance allows us to define a class that inherits all the methods and properties from another class. The Parent class is the class being inherited from, also called base class. Python enables developers to inherit multiple functionalities and properties from different base classes into a single derived class
  
![image](https://user-images.githubusercontent.com/90926526/172481368-e5e49841-44dd-484d-826f-921eab759c27.png)

### Output:
  
![image](https://user-images.githubusercontent.com/90926526/172481621-67b0fc81-fa88-4c00-b21e-2041a374b2f7.png)

![image](https://user-images.githubusercontent.com/90926526/172482458-841c9ba9-f671-42f4-97e6-9841c3eb0bed.png)


## Decorators:
  
A decorator is a function that accepts a function as input and returns a new function as output, allowing us to extend the behavior of the function without explicitly modifying it.
  

### Timer
The @timer decorator reports the execution time of a function. 
It will do the following:

<li> Store the time just before the function execution (Start Time)
<li> Run the function
<li> Store the time just after the function execution (End Time)
<li> Print the difference between two time intervals
<li> Return the modified function for use
  

### Output:

![image](https://user-images.githubusercontent.com/90926526/172482292-92274c39-87b7-4d21-9892-d227f1cefd99.png)

![image](https://user-images.githubusercontent.com/90926526/172482356-43edc724-43a8-428a-b6a5-df8d7c13bc46.png)
