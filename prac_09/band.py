"""
CP1404/CP5632 Practical
Band class to hold a group of musicians.
"""

from musician import Musician


class Band:
    """Represent a band, which consists of multiple musicians."""

    def __init__(self, name):
        """Initialise a Band with a name and an empty list of musicians."""
        self.name = name
        self.members = []

    def add(self, musician):
        """Add a musician to the band."""
        self.members.append(musician)

    def __str__(self):
        """Return string representation of the band and its members."""
        members_str = ", ".join(str(musician) for musician in self.members)
        return f"{self.name} ({members_str})"

    def play(self):
        """Return the play output from all musicians in the band."""
        return "\n".join(musician.play() for musician in self.members)
