"""
example08 -

@IDE:   PyCharm
@Author:石少全
@Date:2022/5/10 15:50 
@Description: ---


"""

year = int(input('Please enter the year you want to check. '))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400:
            print(f'{year} is leap year.')
else:
    print(f'{year} is not a leap year')
