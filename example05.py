"""
example05 -

@IDE:   PyCharm
@Author:石少全
@Date:2022/5/10 14:09 
@Description: ---


"""
print('Welcomd to the rollercoaster!')

height = int(input('What is your height in cm? '))

if height >= 120:
    print('You can ride the rollercoaster!')
    age = int(input('What is your age? '))
    if age < 12:
        print('Please pay 5 yuan!')
    elif age <= 18:
        print('Please pay 7 yuan!')
    else:
        print('Please pay 12 yuan.')
else:
    print('Sorry, you have to grow taller before you can ride.')



