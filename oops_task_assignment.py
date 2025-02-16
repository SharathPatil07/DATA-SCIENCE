# -*- coding: utf-8 -*-
"""OOPS Task Assignment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eQC_LsPfufNz44_joNMWHG6AUne1SFwB
"""

class Vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle

class Car(Vehicle):
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        super().__init__(name_of_vehicle, max_speed, average_of_vehicle)

    def seating_capacity(self, capacity):
        return f"{self.name_of_vehicle} has a seating capacity of {capacity} persons."

# Creating an instance of the Car class
my_car = Car("Honda Civic", 220, 18)

# Accessing the seating_capacity method
print(my_car.seating_capacity(5))

"""In Python, multiple inheritance allows a class to inherit attributes and methods from more than one parent class. This enables the creation of complex relationships and the reuse of code across different classes."""

# Parent class 1
class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")

# Parent class 2
class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap.")

# Child class
class Bat(Mammal, WingedAnimal):
    pass

# Creating an object of the Bat class
bat = Bat()
bat.mammal_info()          # Output: Mammals can give direct birth.
bat.winged_animal_info()   # Output: Winged animals can flap.

"""In Python, getters and setters are methods that allow you to access and modify the attributes of a class, providing a way to implement encapsulation and data validation. While direct access to attributes is common in Python, using getters and setters can be beneficial when you need to add logic during attribute access or assignment."""

class Person:
    def __init__(self, name, age):
        self._name = name  # Note the leading underscore (convention for "protected" attributes)
        self._age = age

    # Getter for 'name'
    @property
    def name(self):
        return self._name

    # Setter for 'name'
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

    # Getter for 'age'
    @property
    def age(self):
        return self._age

    # Setter for 'age'
    @age.setter
    def age(self, value):
        if not isinstance(value, int) or not (0 <= value <= 120):
            raise ValueError("Age must be an integer between 0 and 120.")
        self._age = value

"""
In Python, method overriding occurs when a subclass provides a specific implementation for a method that is already defined in its superclass. This allows the subclass to modify or extend the behavior of the inherited method to suit its own needs. The overridden method in the subclass should have the same name and parameters as the method in the parent class."""

# Parent class
class Animal:
    def speak(self):
        print("The animal makes a sound.")

# Child class
class Dog(Animal):
    def speak(self):
        print("The dog barks.")

# Child class
class Cat(Animal):
    def speak(self):
        print("The cat meows.")

# Creating objects
generic_animal = Animal()
dog = Dog()
cat = Cat()

# Calling the speak method on each object
generic_animal.speak()  # Output: The animal makes a sound.
dog.speak()             # Output: The dog barks.
cat.speak()             # Output: The cat meows.

