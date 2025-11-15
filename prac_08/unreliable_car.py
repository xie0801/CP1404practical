"""
CP1404/CP5632 Practical
UnreliableCar is-a Car but may not always drive.
"""

import random
from car import Car

class UnreliableCar(Car):
    """Represent a car that has a reliability rating affecting drive success."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar with given reliability (0-100)."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car; success depends on reliability.
        Returns the distance driven: either the full possible distance or 0.
        """
        if random.randint(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
