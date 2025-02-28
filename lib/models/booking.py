from models.__init__ import CONN, CURSOR

class Booking:

    all = []
    
    def __init__(self, number_of_tickets, flight_id):
        self.id = None
        self.number_of_tickets = number_of_tickets
        self.flight_id = flight_id
        self.total_price = self.number_of_tickets * (self.flight().price)

    @property
    def number_of_tickets_getter(self):
        return self._number_of_tickets
    
    @number_of_tickets_getter.setter
    def number_of_tickets(self, value):
        if (type(value) == int) and (value > 0):
            self._number_of_tickets = value
        else:
            raise Exception("Error: Number of tickets must be an integer that is greater than 0!")
        
    @property
    def flight_id_getter(self):
        return self._flight_id
    
    @flight_id_getter.setter
    def flight_id(self, value):
        if type(value) == int:
            self._flight_id = value
        else:
            raise Exception("Error: Flight ID must be an integer!")
        
    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY,
                number_of_tickets INTEGER,
                total_price REAL,
                flight_id INTEGER
            )
        '''

        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE IF EXISTS bookings
        '''

        CURSOR.execute(sql)

    def save(self):
        sql = '''
            INSERT INTO bookings (number_of_tickets, total_price, flight_id)
            VALUES (?, ?, ?)
        '''

        CURSOR.execute(sql, (self.number_of_tickets, self.total_price, self.flight_id))
        CONN.commit()

        self.id = CURSOR.lastrowid

        Booking.all.append(self)

    @classmethod
    def create(cls, number_of_tickets, flight_id):
        new_booking = cls(number_of_tickets, flight_id)
        new_booking.save()
        return new_booking

    @classmethod
    def instance_from_db(cls, row):
        new_booking = cls(row[1], row[3])
        new_booking.id = row[0]
        new_booking.total_price = row[2]
        return new_booking
    
    @classmethod
    def get_all(cls):
        sql = '''
            SELECT * FROM bookings
        '''

        rows = CURSOR.execute(sql).fetchall()

        cls.all = [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = '''
            SELECT * FROM bookings
            WHERE id = ?
        '''

        row = CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            return None
        
    def delete(self):
        sql = '''
            DELETE FROM bookings
            WHERE id = ?
        '''

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        Booking.all = [booking for booking in Booking.all if booking.id != self.id]

    def flight(self):
        from models.flight import Flight

        sql = '''
            SELECT * FROM flights
            WHERE id = ?
        '''

        row = CURSOR.execute(sql, (self.flight_id,)).fetchone()

        if row:
            return Flight.instance_from_db(row)
        else:
            return None
        
    def __repr__(self):
        return f"<Booking # {self.id} - Number Of Tickets: {self.number_of_tickets}, Total Price: {self.total_price}, Flight ID: {self.flight_id}>"