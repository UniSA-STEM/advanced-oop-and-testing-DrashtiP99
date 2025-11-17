"""
File: health_system.py
Description: This class represents the individual health records of the animals in the zoo
Author: Drashti Dineshchandra Patel
ID: 110488649
Username: patdy092
This is my own work as defined by the University's Academic Integrity Policy.
"""
from animal import Animal
from abc import ABC, abstractmethod
from datetime import datetime

class IssueType:
    """Constants for the different health issues"""
    INJURY = "Injury"
    ILLNESS = "Illness"
    MENTAL = "Mental"
    ROUTINE_CHECKUP = "Routine Checkup"
    OTHER = "Other"

class HealthRecord:
    """Represents a health record for managing animal health
     Attributes:
        _animal, _issue_type (str), """

    SEVERITY_LVLS = ["low", "medium", "high", "critical"]
    STATUS_OPTIONS = ["Active", "Monitoring", "Resolved"]


    def __init__(self, animal, issue_type,description, recorded_by, severity):
        #check severity level valid and description set
        if severity not in HealthRecord.SEVERITY_LVLS:
            raise ValueError("Invalid Severity Level")

        if not description or not description.strip():
            raise ValueError("Invalid Description")

        #iniate the attributes of a health record
        self._animal = animal
        self._description = description
        self._recorded_by = recorded_by
        self._issue_type = issue_type
        self._severity = severity
        self._date_recorded = datetime.now()
        self._treatment_plan = ""
        self._notes = []
        self._status = "Active"
        self._resolution_date = None


    #define the getters for the private attributes
    def get_animal(self):
        return self._animal

    def get_issue_type(self):
        return self._issue_type

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

    def get_status(self):
        return self._status

    def is_active(self):
        return self._status in ["Active", "Monitoring"]

    def get_resolution_date(self):
        return self._resolution_date


    #set/define the treatment plans and notes per record
    def set_treatment_plan(self, t_plan):
        self._treatment_plan = t_plan

    def add_notes(self, note):
        note_entry = {
            'date': datetime.now(),
            'note': note.strip(),
            'added_by': self._recorded_by,}
        self._notes.append(note_entry)

    def set_status(self, new_status):
        if new_status not in ["Active", "Monitoring", "Resolved"]:
            raise ValueError("Invalid Status")
        old_status = self._status
        self._status = new_status

        #if resolved, then set the resolution date
        if new_status == "Resolved" and self._resolution_date is None:
            self._resolution_date = datetime.now()

        #add note for resolution
        self.add_notes(f"Status updated from {old_status} to {new_status}")

    def resolve_issue(self, resolution_notes):
        self._status = "Resolved"
        self._resolution_date = datetime.now()
        self.add_notes(f"Issue Resolved: {resolution_notes}")

    def update_severity(self, new_level, reason):
        if new_level not in ["Low", "Medium", "High", "Critical"]:
            raise ValueError("Invalid Severity Level")
        old_severity = self._severity
        self._severity = new_level

        self.add_notes(f"Severity updated from {old_severity} to {new_level} due to {reason}")

    def get_time_since_reported(self):
        d = datetime.now() - self._date_recorded
        return d.days

    #method to create full health report

    def get_full_report(self):
        """String Representation of the full report"""
        report = []
        report.append(f"HEALTH RECORD: {self._animal.get_name()}\n")
        report.append(f"Issue Type: {self._issue_type}\n")
        report.append(f"Description: {self._description}\n")
        report.append(f"Severity: {self._severity}\n")
        report.append(f"Status: {self._status}\n")
        report.append(f"Recorded by: {self._recorded_by}\n")
        report.append(f"Date recorded: {self._date_recorded.strftime('%d-%m-%Y')}\n")
        report.append(f"Days since reported: {self.get_time_since_reported()}\n")

        if self._resolution_date:
            report.append(f"Date Resolved: {self._resolution_date.strftime('%d-%m-%Y')}\n")

        if self._treatment_plan:
            report.append(f"Treatment Plan:\n")
            report.append(f"{self._treatment_plan}\n")

        if self._notes:
            report.append(f"Notes:\n")
            report.append(f"{self._notes}\n")

        return "".join(report)


    def __str__(self):
        """Shorter string representation of the health record"""
        return (f"Health Record for {self._animal.get_name()}: {self._description} with Severity level = {self._severity} "
                f"(Date Recorded: {self._date_recorded.strftime('%d/%m/%Y')})")









