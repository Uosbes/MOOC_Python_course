# Write your solution here
att=1
while True:
    pin=input('PIN: ')
    if pin!='4321':
        print ('Wrong')
        att+=1
    elif pin=='4321' and att==1:
        print('Correct! It only took you one single attempt!')
        break
    else:
        print(f'Correct! It took you {att} attempts')
        break