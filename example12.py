"""
@ Author: shishaoquan
@ Time:  
@ Project: 


"""

print('Welcome to the Love Calculator!')
name1 = input('What is your name? \n')
name2 = input('What is their name? \n')
name1_lower = name1.lower()
name2_lower = name2.lower()
print(f'T occurs {name1_lower.count("t")} times')
print(f'R occurs {name1_lower.count("r")} times')
print(f'U occurs {name1_lower.count("u")} times')
print(f'E occurs {name1_lower.count("e")} times')
total_1 = name1_lower.count("t") + name1_lower.count("r") + name1_lower.count("u") + name1_lower.count("e")
print(f'total_1 is {total_1}')

print(f'L occurs {name2_lower.count("l")} times')
print(f'O occurs {name2_lower.count("o")} times')
print(f'V occurs {name2_lower.count("v")} times')
print(f'E occurs {name2_lower.count("e")} times')
total_2 = name2_lower.count("l") + name2_lower.count("o") + name2_lower.count("v") + name2_lower.count("e")
print(f'Total_2 is {total_2}')
final_str = str(total_1) + str(total_2)
score = int(final_str)
if score < 10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif 40 <= score <= 50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}')









