from models.__init__ import CONN, CURSOR

class Flight:
    
    def __init__(self, airline, price, origin, destination):
        self.airline = airline
        self.price = price
        self.origin = origin
        self.destination = destination