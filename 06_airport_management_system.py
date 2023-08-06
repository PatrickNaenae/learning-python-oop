import datetime

class Flight:
    def __init__(self, flight_id, airline, destination, departure_time):
        self.flight_id = flight_id
        self.airline = airline
        self.destination = destination
        self.departure_time = departure_time
        self.passengers = []

    def __str__(self):
        return f"{self.airline} Flight {self.flight_id} to {self.destination} at {self.departure_time}"

    def add_passenger(self, passenger):
        self.passengers.append(passenger)


class Passenger:
    def __init__(self, passenger_id, name, age):
        self.passenger_id = passenger_id
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} (Age: {self.age})"


class Airport:
    def __init__(self, name):
        self.name = name
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def find_flights_by_destination(self, destination):
        matching_flights = []
        for flight in self.flights:
            if flight.destination.lower() == destination.lower():
                matching_flights.append(flight)
        return matching_flights


# Example usage:
flight1 = Flight(101, "Airline A", "New York", datetime.datetime(2023, 8, 10, 8, 30))
flight2 = Flight(102, "Airline B", "London", datetime.datetime(2023, 8, 12, 12, 45))

passenger1 = Passenger(201, "John Doe", 35)
passenger2 = Passenger(202, "Alice Smith", 28)

flight1.add_passenger(passenger1)
flight1.add_passenger(passenger2)

airport = Airport("International Airport")
airport.add_flight(flight1)
airport.add_flight(flight2)

airport_destinations = airport.find_flights_by_destination("New York")
for airport_destination in airport_destinations:
    for passenger in airport_destination.passengers:
        print(passenger)
