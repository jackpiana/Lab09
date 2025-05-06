import datetime
from dataclasses import dataclass

"""
ID
IATA_CODE
AIRPORT
CITY
STATE
COUNTRY
LATITUDE
LONGITUDE
TIMEZONE_OFFSET

ID: int
    AIRLINE_ID: int
    FLIGHT_NUMBER: int
    TAIL_NUMBER: str
    ORIGIN_AIRPORT_ID: int
    DESTINATION_AIRPORT_ID: int
    SCHEDULED_DEPARTURE_DATE: datetime
    DEPARTURE_DELAY: float
    ELAPSED_TIME: int
    DISTANCE: int
    ARRIVAL_DATE: datetime
    ARRIVAL_DELAY: int
"""

@dataclass
class Airport:
    ID: int
    IATA_CODE: str
    AIRPORT: str
    CITY: str
    STATE: str
    COUNTRY: str
    LATITUDE: float
    LONGITUDE: float
    TIMEZONE_OFFSET: float

    def __eq__(self, other):
        return self.ID == other.ID
    def __hash__(self):
        return hash(self.ID)
    def __str__(self):
        return f"{self.ID} - {self.AIRPORT} - {self.CITY}"
