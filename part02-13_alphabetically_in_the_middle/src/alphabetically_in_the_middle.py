# Write your solution here
a=input('1st letter:')
x=input('2nd letter:')
z=input('3rd letter:')
if a<x<z or z<x<a:
   print(f'The letter in the middle is {x}')
if x<a<z or z<a<x:
    print(f'The letter in the middle is {a}')
if a<z<x or x<z<a:
    print(f'The letter in the middle is {z}')