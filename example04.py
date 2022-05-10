"""
example04 -

@IDE:   PyCharm
@Author:石少全
@Date:2022/5/10 11:19 
@Description: ---


"""

print('Welcome to the tip calculator.')
total_bill = input('What was the total bill? ')
percentage = input('What percentage tip would you like to give ? 10, 12, or 15? ')
person_num = input('How many people to split the bill? ')
last_bill = float(total_bill) * (100 + int(percentage))/100
every_cost = last_bill / int(person_num)
last_str = f'Each person should pay: {every_cost:.2f}'
print(last_str)