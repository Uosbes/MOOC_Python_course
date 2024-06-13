# Write your solution here
word=input('Please type in string 1: ')
word2=input('Please type in string 2: ')
if len(word)>len(word2):
    print(f'{word} is longer')
elif len(word2)>len(word):
    print(f'{word2} is longer')
else:
    print('The strings are equally long')