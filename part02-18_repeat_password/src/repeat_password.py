# Write your solution here
passwd=input('Password: ')
passwd1=input('Repeat password: ')
while passwd!=passwd1:
    print('They do not match!')
    passwd1=input('Repeat password: ')
print('User account created!')