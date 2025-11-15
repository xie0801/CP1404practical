"""
CP1404/CP5632 Practical
Test program for the SilverServiceTaxi class.
Verifies fare calculation, rounding, and string output.
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Test the SilverServiceTaxi class with known input and expected output"""
    test_taxi = SilverServiceTaxi("Test Limo", 100, 2)  # fanciness 2 → $2.46/km

    """Start a new fare and drive 18 km (18 * 2.46 + 4.50 = 48.78 → rounded to 48.80)"""
    test_taxi.drive(18)

    assert test_taxi.get_fare() == 48.8, f"Expected $48.80, got ${test_taxi.get_fare():.2f}"
    print("get_fare() test passed")

    """Check __str__ output includes fanciness-based rate and flagfall"""
    expected_str = "Test Limo, fuel=82, odometer=18, 18km on current fare, $2.46/km plus flagfall of $4.50"
    actual_str = str(test_taxi)
    assert actual_str == expected_str, f"\nExpected: {expected_str}\nGot:      {actual_str}"
    print("__str__() test passed")


main()
