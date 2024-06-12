# Write your solution here
days=int(input('How many times a week do you eat at the student cafateria? '))
price=float(input('The prive of a typical student lunch? '))
money_a_week=float(input(' How much money do you spend on groceries in a week? '))

weekly=days*price+money_a_week
daily=weekly/7
print(f"Avarage food expenditure:\nDaily: {daily} euros\nWeekly: {weekly} euros")