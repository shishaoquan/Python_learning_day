"""
example07 -

@IDE:   PyCharm
@Author:石少全
@Date:2022/5/10 14:30 
@Description: --- BMI 2.0


"""

weight = float(input('What is your Weight?(kg) '))
high = float(input('What is your High？(m) '))
bmi = weight/high**2
if bmi < 18.5:
    print('You are underweight.')
elif bmi < 25:
    print('You are normal weight.')
elif bmi < 30:
    print('You are overweight.')
elif bmi < 35:
    print('You are obese.')
else:
    print('You are clinically obese.')