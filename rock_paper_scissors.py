import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input('Type Rock/Paper/Scissors or Q to QUIT:').lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    computer_input = options[random_number]
    print('Computer selected', computer_input + '.')

    if user_input == 'rock' and computer_input == 'scissors':
        print('You win!')
        user_wins += 1
        
    elif user_input == 'paper' and computer_input == 'rock':
        print('You win!')
        user_wins += 1
        
    elif user_input == 'scissors' and computer_input == 'paper':
        print('You win!')
        user_wins += 1
    
    else:
        print('Computer wins!')
        computer_wins += 1

print('Your wins:', user_wins)
print('Computer wins:', computer_wins)
print('Thanks for playing!')