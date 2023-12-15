# building a small tip calculator that asks the total bill how many people will tip and what percentage of tip would you like to include and calculates the earch persons share
# first we are sking the user whats the total bill and taking input from the user using INT input fuction
try:
    total_bill = float(input(" Enter the total bill thats on the receipt :\n "))
    total_people = float(input(" Enter the numer of people in the group :\n ")) #no of people in the group
    total_tip = float(input(" What percentage would you like to tip :\n ")) # total tip that are paying
    total_bill_share = (total_bill + (total_bill*total_tip)/100 )/total_people #logic cacucating tip plus ading it to the total plus didving itby total people 
    print(f"the total share per person is {total_bill_share} ") # printing it out
except:
    print(" Please enter a numeric value ") # using try and excet to chcek for error inputs