"""
File: Enclosure.py
Description: This class represents the enclosures of the animals
Author: Drashti Dineshchandra Patel
ID: 110488649
Username: patdy092
This is my own work as defined by the University's Academic Integrity Policy.
"""
from animal import Animal


class Enclosure:
    """Enclosure for all animals"""

    def __init__(self, enc_id,size, environment, capacity ):
        self._enc_id = enc_id #enclosure ID
        self._size = size
        self._environment = environment
        self._capacity = capacity
        self._cleanliness_lvl = 100
        self._compatible_species = None
        self._animals = []

    #define getters to access private attributes
    def get_enclosure_id(self):
        return self._enc_id

    def get_size(self):
        return self._size

    def get_environment(self):
        return self._environment

    def get_capacity(self):
        return self._capacity

    def get_cleanliness_lvl(self):
        return self._cleanliness_lvl

    def get_animals(self):
        return self._animals.copy()

    def animal_count(self):
        return len(self._animals)

    #Define method to ge the status of the enclosure
    def get_enclosure_status(self):
        """Return detailed status of enclosure and its attributes"""
        status = f"Enclosure ID: {self._enc_id}\n"
        status += f"Size: {self._size}\n"
        status += f"Environment: {self._environment}\n"
        status += f"Capacity %: {self.animal_count()}/{self._capacity}\n"
        status += f"Cleanliness level: {self._cleanliness_lvl}\n"

        if self._animals:
            status += f"Species: {self._compatible_species}\n"
            status += f"Animals: {self._animals}\n"
        else:
            status += f"Animals: None\n"

        return status


    #define methods to add and remove animals from enclosure
    def add_animal(self, animal):
        """Add an animal to the enclosure, checking compatibility, capacity and treatment status"""

        if self.animal_count() >= self._capacity:
            raise ValueError(f"Enclosure = {self._enc_id} is full!")

        if animal.get_treatment_status():
            raise ValueError(f"Cannot move {animal} who is under treatment")

        if self._compatible_species is None:
            self._compatible_species= animal.get_species()
        elif self._compatible_species != animal.get_species():
            raise ValueError(f"Cannot move {animal} who is not compatible with {self._compatible_species}")

        self._animals.append(animal)
        return True

    def remove_animal(self, animal):
        if animal in self._animals:
            self._animals.remove(animal)
            if len(self._compatible_species) == 0:
                self._compatible_species = None
            return True
        return False


    #clean enclosure by inc cleanliness level
    def clean_enclosure(self, amount = 10):
        self._cleanliness_lvl += min(100, self._cleanliness_lvl + amount)

    #enclosure gets dirty overtime and cleanliness decreases
    def dec_cleanliness(self, amount = 5):
        self._cleanliness_lvl -= max(0, self._cleanliness_lvl - amount)

    #define string method enclosure
    def __str__(self):
        return f"Enclosure {self._enc_id} - {self._environment}"






