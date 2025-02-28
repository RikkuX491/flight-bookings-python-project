import sqlite3

CONN = sqlite3.connect('flight_bookings.db')
CURSOR = CONN.cursor()
