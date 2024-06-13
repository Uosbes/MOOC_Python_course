# Write your solution here
string=input('Please type in a word: ')
char=input('Please type in a character: ')


index=string.find(char)
if char in string and len(string[index:index+3])>2:
    print(string[index:index+3])