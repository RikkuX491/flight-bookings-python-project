from models.__init__ import CONN, CURSOR

class Flight:

    all = []
    
    def __init__(self, airline, price, origin, destination):
        self.airline = airline
        self.price = price
        self.origin = origin
        self.destination = destination
        self.id = None

    @property
    def airline_getter(self):
        return self._airline
    
    @airline_getter.setter
    def airline(self, value):
        if (type(value) == str) and (len(value) > 4):
            self._airline = value
        else:
            raise Exception("Error: Airline must be a string that is at least 5 characters long!")
        
    @property
    def price_getter(self):
        return self._price
    

    @price_getter.setter
    def price(self, value):
        if (type(value) in [int, float]) and (value > 0):
            self._price = value
        else:
            raise Exception("Price must be a number that is greater than 0!")
        
    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS flights (
                id INTEGER PRIMARY KEY,
                airline TEXT,
                price REAL,
                origin TEXT,
                destination TEXT
            )
        '''

        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE IF EXISTS flights
        '''

        CURSOR.execute(sql)

    def save(self):
        sql = '''
            INSERT INTO flights (airline, price, origin, destination)
            VALUES (?, ?, ?, ?)
        '''

        CURSOR.execute(sql, (self.airline, self.price, self.origin, self.destination))
        CONN.commit()

        self.id = CURSOR.lastrowid

        Flight.all.append(self)

    @classmethod
    def create(cls, airline, price, origin, destination):
        new_flight = cls(airline, price, origin, destination)
        new_flight.save()
        return new_flight
    
    @classmethod
    def instance_from_db(cls, row):
        new_flight = cls(row[1], row[2], row[3], row[4])
        new_flight.id = row[0]
        return new_flight
    
    @classmethod
    def get_all(cls):
        sql = '''
            SELECT * FROM flights
        '''

        rows = CURSOR.execute(sql).fetchall()

        cls.all = [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = '''
            SELECT * FROM flights
            WHERE id = ?
        '''

        row = CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            return None
        
    def delete(self):
        sql = '''
            DELETE FROM flights
            WHERE id = ?
        '''

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        Flight.all = [flight for flight in Flight.all if flight.id != self.id]

    def __repr__(self):
        return f"<Flight # {self.id} - Airline: {self.airline}, Price: {self.price}, Origin: {self.origin}, Destination: {self.destination}>"