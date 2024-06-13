# Write your solution here

count=""
word1= None
while True :
    word=input('Please type in a word: ')
    if word=='end':
        break
    if word1==word:
        break
    word1=word
    count=count+word+" "
print(count)
        
