#Mariana Guerrero
#Travel Times
#COP 2500C
#July 10, 2024


print("Welcome to travel planner.")

#Get input for both time and number of places.

mins=int(input("How long do you have to visit today?\n"))
num_places=int(input("How many places are you visiting?\n"))

total_mins=0

#For loop because we know how many times we are going to loop.
for count in range(1,num_places+1):
    print("How long does it take to travel to location #",count,"?",sep="")
    commute=int(input())
    print("How long would you like to stay in location #",count,"?",sep="")
    stay=int(input())
    
#Get the total for both commute and tiem staying at the place.
    total_mins+=commute+stay

print("This trip would take",total_mins,"minutes.")

#if statement to check if the trip will be taken on time.
if mins>=total_mins:
        print("You are able to take this trip.")
else:
        print("You are not able to take this trip on time.")
    
