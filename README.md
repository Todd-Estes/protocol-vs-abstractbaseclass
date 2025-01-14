# protocol-vs-abstractbaseclass
-Small project differentiating the AbstractBaseClass and Protocol design patterns in Python. 

-Replicates Internet of Things toy app for each design pattern.

-OOP Concepts (Abstraction, Inheritance and Composition).

https://realpython.com/inheritance-composition-python/

**Main Points about ABC**
---
- Parent ABC cannot be instantiated - only derived subclassed can be instantiated.
- Parent ABC class must explicitly inherit from ABC, and subclasses must explicitly inherit from base parent class.
- Static methods not to be used in base class are decorated with @staticmethod, and use pass placeholder.
- Derived methods are strictly coupled with the base class.
- Python uses **Nominal typing** to check relationship and strict class inheritance in the interpreter.

**Main Points about Protols**
---
- No inheritance relationships - Protocol classes define the interface to the parts of the program that refer to it.
- **Structural Typing** i.e. Duck Typing 🦆 Interpreter checks that Protocol class and derivatives and have structural properties (methods and properties).
- Part of **Interface Segregation** SOLID
  
