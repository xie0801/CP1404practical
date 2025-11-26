"""
CP1404/CP5632 Practical
Test program for the UnreliableCar class.
Verifies that the car sometimes drives and sometimes fails based on reliability.
"""
from unreliable_car import UnreliableCar

def main():
    """Test the UnreliableCar class by simulating multiple drives."""
    reliable_car = UnreliableCar("Reliable Car", 100, 90)   # 90% chance to drive
    unreliable_car = UnreliableCar("Unreliable Car", 100, 10)  # 10% chance to drive

    print("Testing Reliable Car:")
    test_drive(reliable_car, 10, 10)

    print("\nTesting Unreliable Car:")
    test_drive(unreliable_car, 10, 10)


def test_drive(car, distance, attempts):
    """Attempt to drive the car multiple times and display outcomes."""
    for i in range(attempts):
        distance_driven = car.drive(distance)
        print(f"Attempt {i + 1}: {car.name} drove {distance_driven}km (odometer={car.odometer})")


main()
