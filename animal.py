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
        self._health_manager = None

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


#subclasses for specific animals of each species
class Lion(Animal):
    def __init__(self, name, age, pride_member = True):
        super().__init__(
            name = name,
            species = "Lion",
            age = age,
            diet = "Carnivore: 5-7kg of raw meat daily",
        )
        self._pride_member = pride_member

    #override make sound method for lion subclass
    def make_sound(self):
        return f"{self._name} roars!"

    def get_animal_type(self):
        return "Lion"

    def is_pride_member(self):
        return self._pride_member

    def hunt(self):
        """Lions are apex predators so they hunt"""
        if self._pride_member:
            return f"{self._name} hunts with their pride"
        return f"{self._name} hunts alone"

class Python(Reptile):
    """Represents a Python as a reptile species
        unique attribute is length in meters set to default of 3.0"""
    def __init__(self, name, age, length):
        super().__init__(
            name=name,
            species="Australian Scrub",
            age=age,
            diet = "Carnivore: small mammals, lizards and bird every 1-2 weeks",
            venomous=False)
        self._length = length

    #unique getter for this subclass
    def get_length(self):
        return self._length
    #override abstract methods for this subclass
    def make_sound(self):
        return f"{self._name} hisses!"

    def get_animal_type(self):
        return "Python"

    def kill_prey(self):
        """Pythons kill prey by constriction"""
        return f"{self._name} kills prey by constriction"

    def shed_skin(self):
        return f"{self._name} sheds their skin"

    def __str__(self):
        """String representation of python and its characteristics"""
        return f"{super().__str__()} with Length = {self.length}"


    class Parrot(Bird):
        """Parrot subclass with unique attributes of colour and vocab"""
        def __init__(self, name, age, colour="Rainbow"):
            super().__init__(
                name=name,
                species = "Scarlet Macaw",
                age=age,
                diet = "Omnivore: 100-150g of plants, seeds, nuts, and insects",
                can_fly = True
            )
            self._colour = colour
            self._vocabulary = []

        def make_sound(self):
            if self._vocabulary:
                word = self._vocabulary[0]
                return f"Parrot {self._name} squawks {word}!"
            else:
                return f"Parrot {self._name} SQUAWKS!"

        def get_animal_type(self):
            return "Parrot"

        def get_colour(self):
            return self._colour

        def get_vocabulary(self):
            return self._vocabulary

        def teach_word(self, word):
            """Teach the parrot a new word"""
            if word not in self._vocabulary:
                self._vocabulary.append(word)
                return f"{self._name} has learned to say {word}"
            return f"{self._name} already knows {word}"

        def __str__(self):
            """String representation of parrot and its characteristics"""
            vocab_count = len(self._vocabulary)
            return f"{super().__str__()} - colour is {self._colour} and it knows {vocab_count} words"














