"""
CP1404/CP5632 Practical
project.py
Project class representing a software project.
"""

class Project:
    """Represent a Project with name, start_date, priority, cost estimate and completion percentage."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a user-friendly string representation of the project."""
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, complete: {self.completion_percentage}%")

    def __repr__(self):
        """Return a developer-friendly string representation of the project."""
        return (f"Project({self.name!r}, {self.start_date!r}, {self.priority}, "
                f"{self.cost_estimate}, {self.completion_percentage})")

    def __lt__(self, other):
        """Compare Projects by priority for sorting (lower is higher priority)."""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if the project is 100% complete."""
        return self.completion_percentage == 100
