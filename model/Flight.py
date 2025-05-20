from dataclasses import dataclass
from datetime import datetime


@dataclass
class Flight:
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

    def __eq__(self, other):
        return self.ID == other.ID
    def __hash__(self):
        return hash(self.ID)
    def __str__(self):
        return f"{self.FLIGHT_NUMBER} - from: {self.ORIGIN_AIRPORT_ID} to: {self.DESTINATION_AIRPORT_ID}"
