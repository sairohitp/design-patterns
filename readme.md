## Introduction

### Creational Patterns

These patterns help create objects in a flexible way.

1. **Factory Method**: Instead of creating an object directly, we use a method to create the object. This method can create different types of objects without changing the code that calls it.
2. **Abstract Factory**: A factory of factories! It provides methods to create related objects without specifying their concrete classes. Think of it as a kit for assembling various related products.
3. **Builder**: It separates the construction of a complex object from its representation. So, you can create different representations of an object step by step, like assembling a burger with different layers.
4. **Prototype**: Creates new objects by copying an existing object (a prototype). This is useful when object creation is costly, and you need many similar objects.
5. **Singleton**: Ensures a class has only one instance and provides a global point of access to it. For example, a single database connection used throughout the application.

### Structural Patterns

These patterns help compose objects and classes into larger structures while keeping flexibility.

1. **Adapter**: Acts like a translator between two incompatible interfaces. It allows classes with different interfaces to work together by converting one interface to another.
2. **Bridge**: Separates an object’s abstraction from its implementation, allowing them to vary independently. Like separating a remote control (abstraction) from different devices (implementations) it can control.
3. **Composite**: Treats individual objects and compositions of objects uniformly. For example, a folder can contain both files and subfolders, and we can treat both in the same way.
4. **Decorator**: Adds behavior to an object dynamically without altering its structure. Like adding new features to a car without changing the car's original design.
5. **Facade**: Provides a simplified interface to a complex system. Imagine a remote control that simplifies the operation of a complicated home theater system.
6. **Flyweight**: Reduces memory usage by sharing parts of an object that are the same across many instances. It’s like sharing data that doesn’t change, to avoid duplication.
7. **Proxy**: Provides a placeholder for another object to control access to it. For instance, a credit card acts as a proxy for the bank account.

### Behavioral Patterns

These patterns focus on communication between objects.

1. **Chain of Responsibility**: Passes a request along a chain of handlers. Each handler decides whether to process the request or pass it to the next handler.
2. **Command**: Encapsulates a request as an object, allowing the parameterization of clients with different requests and the queuing of requests. For instance, actions like "copy" or "paste" in a text editor.
3. **Interpreter**: Defines a way to evaluate sentences in a language. Used in implementing language interpreters or expression evaluators.
4. **Iterator**: Provides a way to access elements of a collection without exposing its underlying representation. Like browsing through items in a list using "Next" and "Previous" buttons.
5. **Mediator**: Defines an object that manages the communication between different objects to reduce direct dependencies.
6. **Memento**: Allows capturing and restoring an object's state. Think of it like an "Undo" feature in an application.
7. **Observer**: When one object changes, all its dependents are notified automatically. Like how subscribing to a newsletter works; you get updates when there’s new content.
8. **State**: Allows an object to change its behavior when its internal state changes. Like a TV that behaves differently when it's "On" versus "Off."
9. **Strategy**: Enables selecting an algorithm at runtime. It’s like choosing between different sorting methods for an array.
10. **Template Method**: Defines the basic structure of an algorithm, but lets subclasses redefine certain steps. Think of it like a recipe that allows for variation in some ingredients.
11. **Visitor**: Lets you add further operations to objects without changing their classes. It's like hiring different specialists (visitors) to work on the same set of objects.

### Additional Patterns

Theses are not part of the GoF original:

1. **Dependency Injection**: Supplies an object with its dependencies from the outside rather than creating them itself.
2. **Lazy Initialization**: Delays the creation of an object until it is actually needed.
3. **Null Object**: Uses a default "do-nothing" behavior to avoid null checks.
4. **Specification**: Combines business rules by chaining them together for more complex queries.
5. **Double-Checked Locking**: Optimizes lazy initialization in multi-threaded environments to avoid redundant locking.
6. **Extension Object**: Allows an object to have additional functionality without changing its original code.
7. **Policy**: Allows changing behavior dynamically by swapping different policies.
8. **Object Pool**: Manages a pool of reusable objects to avoid costly creation and destruction.
9. **Event Aggregator**: Helps manage events in a system by routing them to subscribers.