"""
File: Zoo.py
Description: This class represents the main management system of the Zoo
Author: Drashti Dineshchandra Patel
ID: 110488649
Username: patdy092
This is my own work as defined by the University's Academic Integrity Policy.
"""
from animal import Animal
from health_record import HealthRecord
from enclosure import Enclosure
from staff import Staff


class Zoo:
    """The main management system for the zoos operations"""
    def __init__(self, name):
        self._name = name
        self._staff = []
        self._animals = []
        self._enclosures = []

    @property
    def name(self):
        return self._name

    #Management of animals - this includes accessing, adding, removing
    def get_animals(self):
        return self._animals.copy()

    def get_animals_species(self, species):
        return [animal for animal in self._animals if animal.get_species() == species]

    def add_animal(self, animal):
        self._animals.append(animal)

    def remove_animal(self, animal):
        if animal in self._animals:
            self._animals.remove(animal)
            return True
        return False

    #staff management - includes adding, removing and getting the staff member
    def get_staff(self):
        return self._staff.copy()

    def add_staff(self, staff):
        self._staff.append(staff)

    def remove_staff(self, staff):
        if staff in self._staff:
            self._staff.remove(staff)
            return True
        return False

    #enclosure management
    def get_enclosures(self):
        return self._enclosures.copy()

    def add_enclosure(self, enclosure):
        self._enclosures.append(enclosure)

    def remove_enclosure(self, enclosure):
        if enclosure in self._enclosures:
            self._enclosures.remove(enclosure)
            return True
        return False

    #methods for reporting of animals, enclosures and health
    def create_animal_report(self):
        report = f"Animal Report:\n"
        report += f"Total Animals = {len(self._animals)}\n"
        report += f"Total Species = {len(self._animals)}\n"

        species_list = set(animal.get_species() for animal in self._animals)

        for species in species_list:
            animals = [a for a in self._animals if a.get_species() == species]
            report += f"{species} ({len(animals)}):\n"
            for animal in animals:
                report += f"  - {animal}\n"
        return report

    def create_health_report(self):
        report = f"Health Report:\n"
        health_issues = False

        for animal in self._animals:
            rec = animal.get_health_report()
            if rec:
                health_issues = True
                report += f"\n{animal.get_name()}:\n"
                for r in rec:
                    report += f"  - {r}\n"
        if not health_issues:
            report += "No Health issues found.\n"
        return report

    def create_enclosure_report(self):
        report = f"Enclosure Report:\n"
        for enc in self._enclosures:
            report += enc.get_enclosure_report() + "\n"
        return report

    def __str__(self):
        """String representation of the overall zoo"""
        animal_num = len(self._animals)
        num_enclosures = len(self._enclosures)
        num_staff = len(self._staff)

        return (f"{self._name} Zoo:\n "
                f"Total Animals = {animal_num}\n"
                f"Total Staff = {num_staff}\n"
                f"Total Enclosures = {num_enclosures}\n")




