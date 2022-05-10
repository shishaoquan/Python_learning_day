"""
example03 -

@IDE:   PyCharm
@Author:石少全
@Date:2022/5/10 11:06 
@Description: ---


"""

# 1 year = 365
# 1 year = 52 week
# 1 year = 12 month


age = input('What is your current_age: \n')

has_year = 90 - int(age)
print(f'you have {has_year} years, and {has_year * 52} week,  and has {has_year * 12} month, and'
      f'has {has_year * 365}days')


age_as_int = int(age)

years_remainint = 90 - age_as_int
days_remainint = years_remainint * 365
weeks_remaining = years_remainint * 52
month_remaining = years_remainint * 12

massage = f'You have {days_remainint} days, {weeks_remaining} weeks, and {month_remaining} months'
print(massage)