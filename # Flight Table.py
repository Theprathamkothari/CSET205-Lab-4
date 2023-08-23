# Flight Table
# Flight ID From To Price
# AI161E90 BLR BOM 5600
# BR161F91 BOM BBI 6750
# AI161F99 BBI BLR 8210
# VS171E20 JLR BBI 5500
# AS171G30 HYD JLR 4400
# AI131F49 HYD BOM 3499
# [BLR: Bengaluru, BOM: Mumbai, BBI: Bhubaneswar, HYD: Hyderabad, JLR: Jabalpur]
# Write a Python program to search and print the result data of the above table.
# User must have option to choose the search parameter
# [1. Flights for a particular City, 2. Flights From a city, 3. Flights between two given
# cities]
# [Write OOP based code.]
class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightDatabase:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def get_flights_for_city(self, city_code):
        return [flight for flight in self.flights if flight.source == city_code or flight.destination == city_code]

    def get_flights_from_city(self, city_code):
        return [flight for flight in self.flights if flight.source == city_code]

    def get_flights_between_cities(self, city_code1, city_code2):
        return [flight for flight in self.flights if flight.source == city_code1 and flight.destination == city_code2]

def main():
    flight_database = FlightDatabase()

    # Add flights to the database
    flight_database.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
    flight_database.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
    flight_database.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
    flight_database.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))
    flight_database.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
    flight_database.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))

    city_data = {
        "BLR": "Bengaluru",
        "BOM": "Mumbai",
        "BBI": "Bhubaneswar",
        "HYD": "Hyderabad",
        "JLR": "Jabalpur"
    }

    while True:
        print("\nOptions:")
        print("1. Flights for a particular City")
        print("2. Flights From a city")
        print("3. Flights between two given cities")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            city_code = input("Enter the city code: ")
            city_flights = flight_database.get_flights_for_city(city_code)
            city_name = city_data.get(city_code)
            if city_name:
                print(f"Flights involving {city_name}:")
                for flight in city_flights:
                    print(f"Flight ID: {flight.flight_id}, From: {flight.source}, To: {flight.destination}, Price: {flight.price}")
            else:
                print("Invalid city code.")

        elif choice == "2":
            city_code = input("Enter the city code: ")
            city_flights = flight_database.get_flights_from_city(city_code)
            city_name = city_data.get(city_code)
            if city_name:
                print(f"Flights from {city_name}:")
                for flight in city_flights:
                    print(f"Flight ID: {flight.flight_id}, To: {flight.destination}, Price: {flight.price}")
            else:
                print("Invalid city code.")

        elif choice == "3":
            city_code1 = input("Enter the first city code: ")
            city_code2 = input("Enter the second city code: ")
            city1_name = city_data.get(city_code1)
            city2_name = city_data.get(city_code2)
            if city1_name and city2_name:
                flights_between = flight_database.get_flights_between_cities(city_code1, city_code2)
                if flights_between:
                    print(f"Flights between {city1_name} and {city2_name}:")
                    for flight in flights_between:
                        print(f"Flight ID: {flight.flight_id}, From: {flight.source}, To: {flight.destination}, Price: {flight.price}")
                else:
                    print(f"No flights found between {city1_name} and {city2_name}.")
            else:
                print("Invalid city code(s).")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
