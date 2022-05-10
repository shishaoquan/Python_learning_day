"""
@ Author: shishaoquan
@ Time:  
@ Project: 


"""

print('Welcome to Python Pizza Deliveries!')
size = input('What size pizza do you want ? S, M, or L ')
add_pepperoni = input('Do you want peperoni? Y or N ')
extra_cheese = input('Do you want extra cheese? Y or N ')
Pizza_bill = 0
if size == 'S':
    Pizza_bill = 15
elif size == 'M':
    Pizza_bill = 20
else:
    Pizza_bill = 25
if add_pepperoni == "Y":
    if size == "S":
        Pizza_bill += 2
    else:
        Pizza_bill += 3

if extra_cheese == 'Y':
    Pizza_bill += 1
print(f'The final Pizza_bill is {Pizza_bill}')







