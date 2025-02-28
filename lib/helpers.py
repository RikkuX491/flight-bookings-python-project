# lib/helpers.py

from models.flight import Flight
from models.booking import Booking

def interact_with_flights_data():
    while True:
        flight_menu()
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            get_all_flights()
        else:
            print("Invalid choice")

def get_all_flights():
    Flight.get_all()

    print("Here is the data for all flights:\n")

    for flight in Flight.all:
        print(flight)

    input("\n-- Enter any key to continue... --\n")

def interact_with_bookings_data():
    while True:
        booking_menu()
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            get_all_bookings()
        else:
            print("Invalid choice")

def get_all_bookings():
    Booking.get_all()

    print("Here is the data for all bookings:\n")

    for booking in Booking.all:
        print(booking)

    input("\n-- Enter any key to continue... --\n")

def exit_program():
    print("Goodbye!")
    exit()

def flight_menu():
    print("Please select an option:")
    print("0. Return to previous menu")
    print("1. Retrieve all flights")

def booking_menu():
    print("Please select an option:")
    print("0. Return to previous menu")
    print("1. Retrieve all bookings")