# Write your solution here
while True:
    num=int(input('Please type in a number: '))
    if num>0:
        index=num
        fract=1
        while index>0:
            fract=fract*index
            index-=1
        print(f'The factorial of the number {num} is {fract}')
    else:
        print('Thanks and bye!')
        break