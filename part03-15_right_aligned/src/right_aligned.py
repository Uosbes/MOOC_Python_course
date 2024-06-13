# Write your solution here
word=input('Please type in a string: ')
x=len(word)
index=20
if x<20:
    print((index-x)*'*'+word)
elif x==index:
    print(word)