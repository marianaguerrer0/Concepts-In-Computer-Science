# Mariana Guerrero
# Flights
# COP 2500C
# June 27, 2024

print("Free Flight Calculator. Follow Steps Down Below!\n")
price = float(input("Enter adult flight cost:\n"))
adult_num = int(input("Number of adults traveling:\n"))
child_num = int(input("Number of children traveling:\n"))
print("Receipt:")

total_ad = print(adult_num, "Adults tickets @ $%.2f"%price,"/each\t$ %.2f" %(price*adult_num))
total_child = print(child_num, "Children tickets @ $%.2f"%(price*0.9),"/each\t$ %.2f" %(price*child_num*0.9))
print("Your Total Comes To\t\t$ %.2f" %((price*adult_num)+(price*child_num*0.9)))
