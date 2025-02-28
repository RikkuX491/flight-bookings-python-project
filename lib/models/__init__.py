import sqlite3

CONN = sqlite3.connect('hotel_reviews.db')
CURSOR = CONN.cursor()
