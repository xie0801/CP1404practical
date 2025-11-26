"""
CP1404/CP5632 Practical
Taxi simulator program using Taxi and SilverServiceTaxi classes.
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    """Run the taxi simulator."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    menu = "q)uit, c)hoose taxi, d)rive"
    print(menu)

    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            if current_taxi:
                total_bill += drive_taxi(current_taxi)
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        print(menu)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

def choose_taxi(taxis):
    """Display list of taxis and allow user to choose one."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid input; enter a number")
    return None

def drive_taxi(taxi):
    """Start a new fare and drive user-defined distance. Return trip cost."""
    taxi.start_fare()
    try:
        distance = float(input("Drive how far? "))
        actual_distance = taxi.drive(distance)
        trip_cost = taxi.get_fare()
        print(f"{taxi.name} drove {actual_distance:.1f}km")
        print(f"Your {taxi.name} trip cost you ${trip_cost:.2f}")
        return trip_cost
    except ValueError:
        print("Invalid input; must be a number")
        return 0.0

def display_taxis(taxis):
    """Display the current state of all taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

main()
