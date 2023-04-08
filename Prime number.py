num =int(input("Enter a number :"))

if num == 1:
    print("It is not a prime number")
if num > 1:
    for i in range(2,num):
        if num % 2 ==0:
            print("This is not a prime number ")
            break 
    else:
      print("It is a prime number")


num = int(input("Enter a number : "))

if num == 1:
    print(num,"is not a prime number")
elif num>1:
    for i in range(2, num):
        if num %2 ==0:
            print(num,"is not a prime number ")
            break
        else:
            print(num,"is a prime number")
