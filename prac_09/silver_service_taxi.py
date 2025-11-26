"""
CP1404/CP5632 Practical
SilverServiceTaxi class derived from Taxi.
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised Taxi with higher fare based on fanciness and a flagfall."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi with fanciness factor."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return fare including flagfall, rounded to nearest 10 cents."""
        return round(super().get_fare() + self.flagfall, 1)

    def __str__(self):
        """Return string representation with flagfall detail appended."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
