year = 1900
if year % 4 == 0:   
  print("Leap year")
elif year % 100 == 0 and year % 400 == 0: 
    print("Leap year") 
else:
  print("Not leap year")