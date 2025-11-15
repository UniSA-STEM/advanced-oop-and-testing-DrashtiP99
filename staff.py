"""
File: Staff.py
Description: This class represents a staff member and the various staff subclasses
Author: Drashti Dineshchandra Patel
ID: 110488649
Username: patdy092
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod

from animal import Animal
from health_record import health_record, HealthRecord


class Staff(ABC):
    """Represents a staff member as an abstract base class"""
    def __init__(self, name, employee_id):
        self._name = name
        self._employee_id = employee_id
        self._assigned_animals = []
        self._assigned_enclosures = []

    #define getters for accessing private attributes above
    def get_name(self):
        return self._name

    def get_employee_id(self):
        return self._employee_id

    def get_assigned_animals(self):
        return self._assigned_animals.copy()

    def get_assigned_enclosures(self):
        return self._assigned_enclosures.copy()

    #abstract methods for different staff
    @abstractmethod
    def get_staff_role(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    #general methods for assigning animals and enclosure to each staff member
    def assign_animal(self, animal):
        if animal not in self._assigned_animals:
            self._assigned_animals.append(animal)
    def assign_enclosure(self, enclosure):
        if enclosure not in self._assigned_enclosures:
            self._assigned_enclosures.append(enclosure)

#define subclasses for unique staff member types like Zookeeper and vet
class ZooKeeper(Staff):
    """Represents a zookeeper member as a subclass of Staff"""
    def __init__(self, name, employee_id):
        super().__init__(name, employee_id)

    def get_staff_role(self):
        return "ZooKeeper"

    #actions for the zookeeper include feeding animals, watering animals, cleaning enclosures, training animals
    def feed_animal(self, animal):
        return f"Zookeeper {self._name} feeds {animal.get_name()}"

    def water_animal(self, animal):
        return f"Zookeeper {self._name} watered {animal.get_name()}"

    def cleanup_animal(self, animal):
        return f"Zookeeper {self._name} cleaned {animal.get_name()}"

    def cleanup_enclosure(self, enclosure):
        enclosure.clean_enclosure()
        return f"Zookeeper {self._name} cleaned Enclosure - {enclosure.get_enclosure()}"

    def train_animal(self, animal):
        return f"Zookeeper {self._name} trained {animal.get_name()}"

class Vet(Staff):
    """"Represents a vet member as a subclass of Staff"""
    def __init__(self, name, employee_id):
        super().__init__(name, employee_id)

    #override get role method for vet
    def get_staff_role(self):
        return "Vet"

    #methods to carry out tasks of the vet like health checks, update treatment plans and creating records
    def complete_health_check(self, animal):
        return f"Vet {self._name} completed health check on {animal.get_name()}"

    def update_treatment_plan(self, health_record, treatment_plan):
        health_record.set_treatment_plan(treatment_plan)

    def create_record(self, animal, description, severity, treatment_plan):
        health_rec = HealthRecord(self._name, description, severity, treatment_plan)

        #add health record to animal
        animal.add_health_record(health_rec)

        return health_rec

    


