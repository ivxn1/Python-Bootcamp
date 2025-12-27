class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin, destination, from_date, return_date, stops):
        self.price = price
        self.departure_airport_code = origin
        self.destination_airport_code = destination
        self.from_date = from_date
        self.return_date = return_date
        self.stops = stops

def find_cheapest_flight(data):
    if not data:
        print("No flights data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    first_flight = data[0]
    cheapest_price = float(first_flight['price']['grandTotal'])
    origin = first_flight['itineraries'][0]['segments'][0]['departure']['iataCode']
    destination = first_flight['itineraries'][0]['segments'][0]['arrival']['iataCode']
    from_date = first_flight['itineraries'][0]['segments'][0]['departure']['at'].split("T")[0]
    return_date = first_flight['itineraries'][0]['segments'][0]['arrival']['at'].split("T")[0]
    stops = len(first_flight['itineraries'][0]['segments']) - 1
    cheapest_flight = FlightData(cheapest_price, origin, destination, from_date, return_date, stops)

    for flight in data:
        curr_price = float(flight['price']['grandTotal'])
        if curr_price < cheapest_price:
            cheapest_price = curr_price
            origin = flight['itineraries'][0]['segments'][0]['departure']['iataCode']
            destination = flight['itineraries'][0]['segments'][0]['arrival']['iataCode']
            from_date = flight['itineraries'][0]['segments'][0]['departure']['at'].split("T")[0]
            return_date = flight['itineraries'][0]['segments'][0]['arrival']['at'].split("T")[0]
            stops = len(flight['itineraries'][0]['segments']) - 1
            cheapest_flight = FlightData(cheapest_price, origin, destination, from_date, return_date, stops)

    print(f"Lowest price to {destination} is {cheapest_flight.price}GBP")
    return cheapest_flight
