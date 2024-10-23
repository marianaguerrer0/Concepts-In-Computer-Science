#Mariana Guerrero
#Travel Distances
#COP 2500C
#July 13, 2024


#Asks user for amount of trips.
num_trip=int(input("How many trips do you have planned?\n"))

#Create empty list
miles=[]

#For loop is used because we know how many times it will loop.
for i in range (num_trip):
    distance=float(input("How many miles is trip #"+str(i+1)+"?\n"))
    miles.append(distance)
#Sorting the list from smallest to largest number.
miles.sort()

#Adds 3 largest values.
total_miles= miles[-3]+miles[-2]+miles[-1]

print("The total distance of the 3 longest trips is",total_miles,"miles.")
