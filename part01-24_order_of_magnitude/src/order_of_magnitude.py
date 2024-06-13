# Write your solution here
num=int(input("Please type in a number: "))
if num<10:
    print("This number is smaller than 1000\nThis number is smaller than 100\nThis number is smaller than 10\nThank you!")
elif 10<=num<100:
    print("This number is smaller than 1000\nThis number is smaller than 100\nThank you!")
elif 100<=num<1000:
    print("This number is smaller than 1000\nThank you!")
else:
    print("Thank you!")