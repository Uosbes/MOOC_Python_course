# Write your solution here
string=input('Please type in a word: ')
char=input('Please type in a character: ')


index=string.find(char)

while char in string:
    if char in string and len(string[index:index+3])>2:
        if string[index]==char:
            print(string[index:index+3])
        else:
            pass
    else:
        break
    string=string[1:]
    