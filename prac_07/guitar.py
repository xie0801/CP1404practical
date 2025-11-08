"""
CP1404/CP5632 Practical
guitar.py
Class for representing a guitar and its properties.
"""

from datetime import date

class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Return the age of the guitar in years."""
        current_year = date.today().year
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old."""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Compare guitars by year for sorting (older < newer)."""
        return self.year < other.year

    def __str__(self):
        """Return string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"
