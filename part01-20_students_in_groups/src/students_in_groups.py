# Write your solution here
students=int(input('How many students on the course? '))
groups=int(input('Desired group size? '))
if students%groups==0:
    print (f"Number of groups formed: {students//groups}")
else:
    print (f"Number of groups formed: {(students//groups)+1}")