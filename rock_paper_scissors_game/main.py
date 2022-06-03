#Title: Rock Paper Scissors Game

# Summary:
# rock beats scissors
# scissors beats paper
# paper beats rock

# import the random module
import random

# fn:the game
def rock_paper_scissors_game():
    # intro, options & player selection
    print('Starting the Rock Paper Scissors game!')
    
    game_option = ['R', 'P', 'S']

    print('Select an option: (R: Rock, P: Paper, S: Scissors)')
    # getting user choice
    user_choice = input('Please enter a letter (R, P or S): ').upper()

    # calls fn & check pass 
    if check_player(user_choice):
        # random choice for computer
        computer = random.choice(game_option)

        print('Player(' + check_player(user_choice) + '):' + 'CPU(' + check_player(computer) + ')')

        winner = display_winner(user_choice, computer)
    return winner

# fn:check and print players choice
def check_player(player):
    game_option = ['Rock', 'Paper', 'Scissors']
    
    for i in game_option:
        if player == 'R':
            chosen = game_option[0]
        elif player == 'P':
            chosen = game_option[1]
        elif player == 'S':
            chosen = game_option[2]
        else:
            # repeats user option if true
            print('Invalid letter')
            user_choice = input('Please enter a letter (R, P or S): ').upper()
    return chosen
    

# fn: check & display winner
def display_winner(user, computer):
    # restart game
    if user == computer:
        print('Draw')
        return rock_paper_scissors_game()
    elif user == 'R' and computer == 'S':
        return 'You win'
    elif user == 'S' and computer == 'P':
        return 'You win'
    elif user == 'P' and computer == 'R':
        return 'You win'
    else:
        return 'You loose'

# start game
print(rock_paper_scissors_game())





