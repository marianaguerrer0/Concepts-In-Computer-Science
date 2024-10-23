# Mariana Guerrero
# COP 2500
# Airport Database
# July 25, 2024


#Defing functions.
def menu():
    print("Main menu")
    print("1. Add airport")
    print("2. Remove airport")
    print("3. Access")
    print("4. List Airports")
    print("5. Exit")
    choice = int(input("What would you like to do?\n"))
    return choice

#Adding new airport.
def add_airport(airports):
    code = input("What is the airport´s code?\n")
    name = input("What is the airport´s name?\n")
    distance = int(input("What is the distance from Orlando?\n"))
    airports[code] = dict(name=name, distance=distance)
    print("Added")

#Removing airport.
def remove_airport(airports):
    code = input("What airport would you like to remove?\n")
    if code in airports:
        airports.pop(code) #Using .pop to remove from list.
        print("Airport removed")
    else:
        print("Airport not found")

#Accessing Airport name and distance from the code.
def access_airport(airports):
    code = input("What is the airport code you would like to access?\n")
    if code in airports:
        airport = airports[code]
        print(airport['name'] + " - " + str(airport['distance']) + " miles")
    else:
        print("Airport not found")

#List all airports.
def list_airports(airports):
    if (len(airports)==0):
        print("No Airports")
    else:
        for code in airports:
            print(code + " - " + airports[code]['name'])


def main():
    print("Welcome to Orlando International Airport!")
    airports={} #Creating empty dictionary.

    option=menu()
    while(option !=5):
        if(option==1):
            add_airport(airports)
        if(option==2):
            remove_airport(airports)
        if(option==3):
            access_airport(airports)
        if(option==4):
            list_airports(airports)
        option=menu()

    print("Goodbye")

main()
        
