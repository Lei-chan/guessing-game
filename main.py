import random
    
max_attemps = 5
user_attemps = 1    
nuts = ['hazelnut', 'almond', 'pistacho', 'walnut', 'pecan', 'cashew']

last_index = len(nuts) - 1
random_index = random.randint(0, last_index)
treat = nuts[random_index]

print(f'Pick a number between 0 and {last_index}! If you could pick a correct number, you can get a treat! You can try {max_attemps} times!')
guess = int(input(f'Pick a number : '))

while random_index != guess and max_attemps != user_attemps:
    attemps_left = max_attemps - user_attemps
    if random_index < guess:
        print('Choose a lower one!')
    else:
        print('Choose a higher one!')
    user_attemps += 1
    guess = int(input(f'Try again! (You can try {attemps_left} more times) :'))
    print('Please type a number')

if random_index == guess:
    print(f'You picked a correct number!! I give you {'an' if treat.startswith('a') else 'a'} {treat} as a treat 😋')
else:
    print(f"Game over 😭 You've tried {max_attemps} times!")

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