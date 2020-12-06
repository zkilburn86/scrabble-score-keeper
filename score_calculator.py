import validation_helper
from game_objects import Player


input('Welcome to Scrabble Score Keeper. Press Enter to Begin')
print('-\n--\n---\n----\n')

number_of_players = 0
players = []

valid_number_of_players = True

try:
    number_of_players = int(input('How many players? '))
except ValueError:
    print('Please enter a number between 1 and 4')
    number_of_players = 0
    valid_number_of_players = False

if number_of_players > 4:
    valid_number_of_players = False

while not valid_number_of_players:
    if number_of_players > 4:
        print('Please enter a number between 1 and 4\n')
    
    try:
        number_of_players = int(input('How many players? '))
        if number_of_players > 4:
            valid_number_of_players = False
        else:
            valid_number_of_players = True
    except ValueError:
        print('Please enter a number between 1 and 4')
        number_of_players = 0
        valid_number_of_players = False

for i in range(number_of_players):
    name = input('Enter player ' + str(i + 1) + '\'s name.\n')
    new_player = Player(name,(i+1),0)
    players.append(new_player)
    print('\n')

game_is_active = True 
order_index = 0

while game_is_active:
    current_player = players[order_index]
    valid_score = False
    proceed_to_next_player = False

    print(current_player.name + '\'s turn\n')

    while not valid_score:
        score = input('Enter score: ("s" to skip, "e" to end game)\n')
        valid_score = validation_helper.is_number(score)
        if score.lower() == 'e':
            game_is_active = False
            break
        if score.lower() == 's':
            proceed_to_next_player = True 
            break 
        if not valid_score:
            print('Please enter a valid number.\n')
        else:
            current_player.score += int(score)
            proceed_to_next_player = True
    
    if proceed_to_next_player:
        if order_index == (number_of_players - 1):
            order_index = 0
        else:
            order_index += 1

    print('Current Scores:\n')
    for person in players:
        print(person.name, ' = ', person.score, '\n')
