from models.flight import Flight
from models.booking import Booking

def seed_database():
    Booking.drop_table()
    Flight.drop_table()

    Flight.create_table()
    Booking.create_table()

    Flight.create("Emirates", 2523.34, "Newark, NJ (EWR)", "Athens, Greece (ATH)")
    Flight.create("JetBlue", 748.23, "Jamaica, NY (JFK)", "Nassau, Bahamas (NAS)")

    Booking.create(2, 1)
    Booking.create(3, 1)
    Booking.create(3, 2)

    print("🌱 Flights and Bookings successfully seeded! 🌱")

seed_database()