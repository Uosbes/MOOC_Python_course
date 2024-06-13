# Write your solution here
num=int(input('Please type in a number: '))
i=1
o=1
while i<=num:
    while o<=num:
        print(f'{i} x {o} = {i*o}')
        o+=1
    o=1
    i+=1

