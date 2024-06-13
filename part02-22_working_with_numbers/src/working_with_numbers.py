# Write your solution here
print('Please type in integer numbers. Type in 0 to finish.')
count=0
numsum=0
negnum=0
posnum=0
while True:
    num=int(input('Number:'))
    count+=1
    numsum=numsum+num
    if num>0:
        posnum+=1
    if num<0:
        negnum+=1
    if num==0:
        print(f'Numbers typed in {count-1}')
        print(f'The sum of the numbers is {numsum}')
        print(f'The mean of the numbers is {numsum/(count-1)}')
        print(f'Positive numbers {posnum}')
        print(f'Negative numbers {negnum}')
        break
