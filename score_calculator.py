import validation_helper
from game_objects import Player


input('Welcome to Scrabble Score Keeper. Press Enter to Begin')
print('-\n--\n---\n----\n')

number_of_players = 0
players = []

valid_number_of_players = False

while not valid_number_of_players:
    number_of_players = input('How many players? ')

    valid_number_of_players = validation_helper.is_valid_number_of_players(number_of_players)

    if not valid_number_of_players:
        message = validation_helper.number_of_players_validity_message(number_of_players)
        print(message + '\n')
        number_of_players = 0
    else:
        number_of_players = int(number_of_players)

for i in range(number_of_players):
    name = input('\nEnter player ' + str(i + 1) + '\'s name.\n')
    new_player = Player(name,(i+1),0)
    players.append(new_player)

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

        if validation_helper.is_exit(score):
            game_is_active = False
            break

        if validation_helper.is_skip(score):
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

    print('\nCurrent Scores:\n')
    for person in players:
        print(person.name, ' = ', person.score, '\n')
