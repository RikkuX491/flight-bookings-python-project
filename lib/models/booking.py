from models.__init__ import CONN, CURSOR

class Booking:
    
    def __init__(self, number_of_tickets, flight_id):
        self.id = None
        self.number_of_tickets = number_of_tickets
        self.total_price = None
        self.flight_id = flight_id

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
        
    def __repr__(self):
        return f"<Booking # {self.id} - Number Of Tickets: {self.number_of_tickets}, Total Price: {self.total_price}, Flight ID: {self.flight_id}>"