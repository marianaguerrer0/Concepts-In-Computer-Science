#Mariana Guerrero
#Airport Names
#COP2500
#July 20, 2024

print("Welcome to Airport Code Finder!")
#Defining Function before using it, with 3 parameters.
def airport_code_finder(airport,city,method):
    #Method 1: NAME.
    if (method=="name"):
        word = airport.split()
        if len(word) >= 3:
            #Looking for uppercases on each word.
            if len(word[0]) >= 2 and word[0][0].isupper() and word[0][1].isupper():
                return word[0][0] + word[0][1] + word[0][2]
            else:
                return word[0][0] + word[1][0] + word[2][0]
        else:
            return word[0][0] + word[1][0] + word[2][0]
    #Method 2: CITY.   
    elif method == "city":
        #Taking first three letters of the word and making them uppercase.
        return city[0:3].upper()
    else:
        #User chose an invalid method.
        print("Choose a valid method: name or city.")
#Defining main Function
def main():
    name=input("Name of airport:\n")
    city=input("Name of city:\n")
    method=input("Coding method (name or city):\n")

    code = airport_code_finder(name, city, method)
    print(name," - ",city," - ", code)

main()
    


    
