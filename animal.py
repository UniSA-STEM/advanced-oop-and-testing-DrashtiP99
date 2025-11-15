"""
File: animal.py
Description: This is the base animal class with subclasses for the different animals.
Author: Drashti Dineshchandra Patel
ID: 110488649
Username: patdy092
This is my own work as defined by the University's Academic Integrity Policy.
"""

from abc import ABC, abstractmethod
from datetime import datetime


class Animal(ABC):
    """Base class for all animals"""

    #initalise all attributes of an animal
    def __init__(self, name, species, age, diet):
        self._name = name
        self._species = species
        self._age = age
        self._diet = diet
        self._health_record = []
        self._treatment_status = False

    #define getter methods to access private attributes
    def get_name(self):
        return self._name

    def get_species(self):
        return self._species

    def get_age(self):
        return self._age

    def get_diet(self):
        return self._diet

    def get_health_record(self):
        return self._health_record

    def get_treatment_status(self):
        return self._treatment_status

    #define setters for attributes that need to changed regularly (age, health record, treatments)
    def set_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age

    def set_health_record(self, health_record):
        self._health_record.append(health_record)

        #if severe condition in record -> need to be under treatment
        if health_record.get_severity() in ["High", "Critical"]:
            self._treatment_status = True

    #clear treatment status back to normal post-treatment
    def clear_treatment(self):
        self._treatment_status = False

    #methods same for all animals
    def eat(self):
        return f"{self._name} is eating {self._diet}"

    def sleep(self):
        return f"{self._name} is sleeping"

    #create string representation for all animals with name, age and species
    def __str__(self):
        return f"Animal name:{self._name}, species:{self._species}, age:{self._age}"

    #Abstract methods for unique animal subclasses
    #method for animal makes sound
    @abstractmethod
    def make_sound(self):
        pass
    @abstractmethod
    #method to get animal type
    def get_animal_type(self):
        pass

#animal subclasses for the categories: mammal, bird,reptile (maybe add fish and insect)
class Mammal(Animal):
    def __init__(self, name, species, age, diet, fur=None):
        super().__init__(name, species, age, diet)
        self._fur = fur

    #getter for attribute = fur colour
    def get_fur(self):
        return self._fur

    #unique abstract method application for this class
    def make_sound(self):
        return f"{self._name} makes a mammal sound!" #this can be overridden

    def get_animal_type(self):
        return "Mammal"

class Bird(Animal):
    def __init__(self, name, species, age, diet, can_fly=True):
        super().__init__(name, species, age, diet)
        self._can_fly = can_fly

    # getter for attribute = flying ability
    def can_fly(self):
        return self._can_fly

    #abstract method application for this subclass
    def get_animal_type(self):
        return "Bird"

    def make_sound(self):
        return f"{self._name} chirps!"

class Reptile(Animal):
    def __init__(self, name, species, age, diet, venomous=False):
        super().__init__(name, species, age, diet)
        self._venomous = venomous

    def is_venomous(self):
        return self._venomous

    def get_animal_type(self):
        return "Reptile"

    def make_sound(self):
        return f"{self._name} hisses!"











