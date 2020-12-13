import urllib.request, urllib.parse
import ssl
import re
import json

URL = 'http://www.massport.com/logan-airport/flights/' # Logan Airport Website
json_text = urllib.request.urlopen(URL, context=ctx).read().decode() # reading json information from site
result = re.findall('.+{*?}', json_text)

json_string = ''

for item in result: # removing blank space and getting the json object holding the flights
    if ("var flights" in item):
        json_string = item[22::]

info = json.loads(json_string) # loading json information for the flights into a dictionary

flight_list = info['Flights']['Flights'] # all flights accessible from the site
flight_arrived_list = [fl for fl in flight_list if fl['Arrived']] # flights which arrived at Logan Airport
boston_flights = [fl for fl in flight_list if fl['DestinationCity'] == 'Boston'] # flights to boston

# printing selected information 
def printFlights(flights):
    output = "Flights\n-----------------------------\n"
    for f in flights:
        output+= ("Flight Number: " + f['FlightNumber'] +
        "\nFrom: " + f['OriginCity'] + "    To: " + f['DestinationCity'] +
        "\nArrived: " + str(f['Arrived']) + "\n\n")
    print(output)

# prints all flights
# printFlights(flight_list)

# prints all arrived flights
printFlights(flight_arrived_list)