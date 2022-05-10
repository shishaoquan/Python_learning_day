"""
example05 -

@IDE:   PyCharm
@Author:石少全
@Date:2022/5/10 14:09 
@Description: ---


"""
print('Welcomd to the rollercoaster!')

height = int(input('What is your height in cm? '))
bill = 0
if height >= 120:
    print('You can ride the rollercoaster!')
    age = int(input('What is your age? '))
    if age < 12:
        bill = 5
        print('Child tickets are 5 yuan!')
    elif age <= 18:
        bill = 7
        print('Youth tickets are 7 yuan!')
    elif age > 45 and age < 55:
        bill = 0
        print('Your tickets are 0 yuan!')
    else:
        bill = 12
        print('Adult tickets are 12 yuan.')
    wants_photo = input('Do you want a photo taken? Y or N.')
    if wants_photo == 'Y':
        # Add three 3 to bill
        bill += 3
    else:
        pass
    print(f'Your final bill is {bill}')
else:
    print('Sorry, you have to grow taller before you can ride.')
