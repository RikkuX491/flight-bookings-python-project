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