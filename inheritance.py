#!/usr/bin/env python

# class animal is the parent class(super class)
class Animal:

    # class atrribute
    name = " "

    # class method
    def eat(self):
        print("I can eat")

# child class or subclass
class Dog(Animal):

    def dog_name(self):
        print(f"the name of my Dog is {self.name}")

# create an object of the subclass(child class)
germanShepherd = Dog()

# access child class method

germanShepherd.name = "scooby"
germanShepherd.eat()