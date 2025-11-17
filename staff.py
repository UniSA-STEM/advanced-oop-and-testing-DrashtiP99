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
from health_system import HealthRecord,IssueType



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

#this is connected to the health management system (as the manager)

class Vet(Staff):
    """Represents a vet member as a subclass of Staff with health management responsibilities"""
    def __init__(self, name, employee_id):
        super().__init__(name, employee_id)

    #override get role method for vet
    def get_staff_role(self):
        return "Vet"

    def create_record(self, animal,issue_type, description, severity):
        """create a comprehensive health record for animal"""
        health_rec = HealthRecord(
            animal=animal,
            issue_type= issue_type,
            description=description,
            recorded_by=self._name,
            severity=severity
        )

        #add health record to animal
        animal.add_health_record(health_rec)

        return health_rec

#methods for health analysis and history

    def get_active_issue(self, animal):
        """Get active health issues for given animal"""
        return [record for record in animal.get_health_record() if record.is_active()]

    def get_critical_issues(self, animal):
        """Get critical health issues for given animal"""
        return [record for record in animal.get_health_record() if record.is_active() and record.get_severity() in ["High","Critical"]]


    def get_health_history(self, animal):
        """Get health history for given animal"""
        recs = animal.get_health_record()
        if not recs:
            return f"{animal.get_name()} has no existing health records"

        history = []
        history.append(f"Health History for {animal.get_name()}:\n")
        history.append(f"Total records = {len(recs)}\n")

        active = [r for r in recs if r.is_active()]
        resolved = [r for r in recs if r.get_status() == "Resolved"]

        history.append(f"Total Active Health Issues = {len(active)}\n")
        history.append(f"Total Resolved Health Issues = {len(resolved)}\n")

        if active:
            history.append(f"List of Active Issues:")
            for record in active:
                history.append(f" - {record}")
        if resolved:
            history.append(f"List of Resolved Issues:")
            #show 3 most recent resolved issues
            for record in resolved[-3]:
                history.append(f" - {record}")

        return "".join(history)


#conuct health check and manage treatment and methods to carry out tasks of the vet like health checks, update treatment plans and treatment management

    def conduct_health_check(self, animal):
        """Conduct a routine health check on given animal"""
        #check if animal has pre-existing health issues
        active_issues = self.get_active_issue(animal)

        if active_issues:
            return (f"Dr.{self._name} has conducted health check on {animal.get_name()}"
                    f"Number of active issue(s) found: {len(active_issues)}")
        else:
            return f"Dr.{self._name} has conducted health check on {animal.get_name()} with no active issue(s) detected"

    def complete_health_check(self, animal):
        return f"Vet {self._name} completed health check on {animal.get_name()}"


    def set_treatment_plan(self, health_record,treatment_plan):
        """set or update treatment plan for given health_record"""
        health_record.set_treatment_plan(treatment_plan)
        return f"Dr.{self._name} set treatment plan for {health_record.get_animal().get_name()}"

    def add_follow_up_note(self, health_record, note):
        health_record.add_note(note, added_by=self._name)
        return f"Dr.{self._name} add follow_up note for {health_record.get_animal().get_name()}"

    #add methods for prescribing meds and treatments
    def prescribe_meds(self, health_record, medication, dosage, frequency, duration):
        """Prescribe medication for given health_record with name, dosage, frequency and duration in days
        Returns the prescription confirmation"""

        prescription = f"{medication} - Dosage {dosage} - Frequency {frequency} - Duration: {duration} days"
        note = f"Prescribed medication: {prescription}"
        health_record.add_note(note, added_by=self._name)

        return f"Dr.{self._name} prescribed medication ({medication}) for {health_record.get_animal().get_name()})"

    def schedule_surgery(self, animal, surgery, date, notes=""):
        """Schedule a specific surgery for given animal and set date, add notes and return confirmation message"""
        description = f"Scheduled Surgery: {surgery}"
        if notes:
            description += f"\nNotes: {notes}"

        record = self.create_record(
            animal,
            IssueType.OTHER,
            description,
            "High"
        )

        plan = f"Scheduled Surgery on {date.strftime('%d/%m/%Y')} - Surgery Type: {surgery}"
        self.set_treatment_plan(record, plan)

        return f"Surgery scheduled for {animal.get_name()} on {date.strftime('%d/%m/%Y')}"


    #define methods for post-treatment changes in severity levels and resolve health issues
    def resolve_health_issue(self, health_record, resolution_notes):
        """Mark a health issue as resolved and return confirmation message"""
        animal = health_record.get_animal()
        health_record.resolve_issue(animal, resolution_notes)

        active_severe_issue = self.get_critical_issues(animal)
        if not active_severe_issue:
            animal._status = False
        return f"Dr.{self._name} resolved health issue for {animal.get_name()}"











