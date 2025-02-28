from models.flight import Flight
from models.booking import Booking

def seed_database():
    Flight.drop_table()
    Flight.create_table()

    Flight.create("Emirates", 2523.34, "Newark, NJ (EWR)", "Athens, Greece (ATH)")
    Flight.create("JetBlue", 748.23, "Jamaica, NY (JFK)", "Nassau, Bahamas (NAS)")

    print("🌱 Flights successfully seeded! 🌱")

seed_database()