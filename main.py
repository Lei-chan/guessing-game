import random
    
nuts = ['hazelnut', 'almond', 'pistacho', 'walnut', 'pecan', 'cashew']

last_index = len(nuts) - 1
random_index = random.randint(0, last_index)

print(f'Pick a number between 0 and {last_index}! If you could pick a correct number, you can get a treat!')
guess = int(input(f'Pick a number : '))

while random_index != guess:
    if random_index < guess:
        print('Choose a lower one!')
    else:
        print('Choose a higher one!')
    guess = int(input('Try again! :'))

treat = nuts[random_index]
print(f'You picked a correct number!! I give you {'an' if treat.startswith('a') else 'a'} {treat} as a treat 😋')


# random_number = random.randint(1, 10)
# print('I pick a number between 1 and 10!')
# guess = int(input('Guess a number :'))

# while random_number != guess:
#   if random_number < guess:
#         print('Too high!')
#   else: 
#         print('Too low!')
#   guess = int(input('Try again :'))

# print(f'Correct 🎉 The number was {random_number}')