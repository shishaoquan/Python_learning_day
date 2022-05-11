"""
example14 -

@IDE:   PyCharm
@Author:石少全
@Date:2022/5/11 11:21 
@Description: 


"""

import random
import my_module

# random_integer = random.randint()

# print(my_module.pi)

random_float = random.random()*5
print(random_float)


love_score = random.randint(1, 100)
print(f'Your love socre si {love_score}')


import random

random_side = random.randint(0,1)
if random_side == 1:
    print("Heads")
else:
    print('Tails')













