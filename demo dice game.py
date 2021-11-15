#ice simple programme -
# User throws Dice --> number -
# User inputs a number 
# Number(Dice) == number
# user wins else lose
# 3 chances are given D
import random
dice = random.randint(1,6) # random.random()  {0,1} float
print("🎲 GAME Choose a random number and be the winner\n") 
print(dice)

def UserOperations():
    user_input = int(input("Gues any number between 1 and 6:   ")) 
    print(user_input)
    if dice == user_input:
        return True
    else:
        return False
        
for 
ktm-vkze-biw