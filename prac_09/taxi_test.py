"""
CP1404/CP5632 Practical
Test program for the Taxi class.
Tests Taxi functionality including driving, fare calculation and fare reset.
"""

from taxi import Taxi

def create_taxi():
    """Create a Taxi object with name 'Prius 1' and 100 units of fuel."""
    return Taxi("Prius 1", 100)

def first_drive(taxi):
    """Drive the taxi 40 km and display its details and current fare."""
    taxi.drive(40)
    print(taxi)
    print(f"Current fare: ${taxi.get_fare():.2f}")

def second_drive(taxi):
    """Start a new fare, drive 100 km and display the taxi and fare details."""
    taxi.start_fare()
    taxi.drive(100)
    print(taxi)
    print(f"Current fare: ${taxi.get_fare():.2f}")

def main():
    """Test the Taxi class by simulating two drives."""
    taxi = create_taxi()
    first_drive(taxi)
    second_drive(taxi)

main()
