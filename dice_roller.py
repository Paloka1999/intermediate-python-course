import random

dice_sum = 0
dice_rolls = int(input('How many dice would you liek to roll? '))
dice_size = int(input('How many sides are the dice? '))
for i in range(0,dice_rolls):
    roll = random.randint(1,dice_size)
    dice_sum += roll
    if roll == 1:
        print(f'You rolled a {roll}! Critical Fail')
    elif roll == dice_size:
        print(f'You rolled a {roll}! Critical Success!')
    else:
        print(f'You rolled a {roll}')
print(f'YOu have rolled a total of {dice_sum}')

#def main():
    #roll = random.randint(1,6)
    #print(f'You rolled a {roll}')

#if __name__== "__main__":
    #main()
