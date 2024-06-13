# Write your solution here
num=int(input('Limit: '))
start=1
suma=1
babu=""
while num>suma:
    babu=babu+str(start)+' + '
    start+=1
    suma=suma+start
       
    
print(f"The consecutive sum: {babu}{start} = {suma}")