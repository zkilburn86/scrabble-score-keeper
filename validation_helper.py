

def is_number(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

def is_exit(entry):
    if entry.lower() == 'e':
        return True
    else:
        return False

def is_skip(entry):
    if entry.lower() == 's':
        return True
    else:
        return False

def number_of_players_validity_message(number_of_players):
    if is_number(number_of_players):
        num = int(number_of_players)
        if num > 4 or num < 2:
            return 'Please enter a number between 1 and 4'
    else:
        return 'Not a valid number'

def is_valid_number_of_players(number_of_players):
    if is_number(number_of_players):
        num = int(number_of_players)
        if num > 4 or num < 2:
            return False 
        return True
    else:
        return False