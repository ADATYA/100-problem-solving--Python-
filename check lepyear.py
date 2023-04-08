year=int(input("Enter your year:"))

if(year % 400 ==0 ) and (year %100==0):
    print(year,"Leap year")
elif(year %4==0 )and(year %100 !=0):
    print(year,"Leap year")

else:
    print(year,'Is not leap year')