# num1=int(input("Enter 1st number :"))
# num2=int(input("Enter 2nd number :"))
# num3=int(input("Enter 3rd number :"))

# if (num1>num2) and (num1>num3):
#     print(num1,"is lergest ")
# elif (num2>num1) and (num2 >num3):
#     print(num2,"is gretter")
# else:
#     print(num3,'is lergest')

n = int(input("enter first dictionary value:"))
dict = {}

for i in range(1, n+1):
    # here i have taken keys as strings
    keys = input("Enter the key item :")
    # here i have taken values as integers
    values = (input("Enter the value item :"))

    dict[i] = dict[keys] = values

 # d = dict[i]
x = int(input("iput the next dictionary"))
for m in range(1, x+1):
    # here i have taken keys as strings
    keys = input("Enter the key item :")
    # here i have taken values as integers
    values = (input("Enter the value item :"))

    dict[m] = dict[keys] = values

print(f"Dict :{dict}")