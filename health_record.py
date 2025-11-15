"""
File: health_record.py
Description: This class represents the individual health records of the animals in the zoo
Author: Drashti Dineshchandra Patel
ID: 110488649
Username: patdy092
This is my own work as defined by the University's Academic Integrity Policy.
"""
from animal import Animal
from abc import ABC, abstractmethod
from datetime import datetime

class HealthRecord:

    SEVERITY_LVLS = ["low", "medium", "high", "critical"]

    def __init__(self, animal, description, recorded_by, severity):
        #check severity level valid
        if severity not in HealthRecord.SEVERITY_LVLS:
            raise ValueError("Invalid Severity Level")

        #iniate the attributes of a health record
        self._animal = animal
        self._description = description
        self._recorded_by = recorded_by
        self._severity = severity
        self._date_recorded = datetime.now()
        self._treatment_plan = ""
        self._notes = []

    #define the getters for the private attributes
    def get_animal(self):
        return self._animal

    def get_description(self):
        return self._description

    def get_recorded_by(self):
        return self._recorded_by

    def get_severity(self):
        return self._severity

    def get_date_recorded(self):
        return self._date_recorded

    def get_treatment_plan(self):
        return self._treatment_plan

    def get_notes(self):
        return self._notes

    #set/define the treatment plans and notes per record
    def set_treatment_plan(self, t_plan):
        self._treatment_plan = t_plan

    def set_notes(self, note):
        self._notes = note

    #represent record as string
    def __str__(self):
        return (f"Health Record for {self._animal.get_name()}: {self._description} with Severity level = {self._severity} "
                f"(Date Recorded: {self._date_recorded.strftime('%d/%m/%Y')})")








