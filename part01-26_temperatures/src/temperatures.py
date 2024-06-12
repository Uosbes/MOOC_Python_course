# Write your solution here
a=float(input("Please type in a temperature (F): "))
cel=(a-32)/1.8
if  cel >= 0:
    print(f"{a} degrees Fahrenheit equals {cel} degrees Celsius")
else:
    print(f"{a} degrees Fahrenheit equals {cel} degrees Celsius\nBrr! It's cold in here!")