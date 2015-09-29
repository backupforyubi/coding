# My Rock-paper-scissors-lizard-Spock project
# Author biyu
# Email yubi@foxmail.com
# Date 2015-07-22

import random

def name_to_number( name ):
# convert name to number, tolerance for upper or lower case:
#    0 — rock
#    1 — Spock
#    2 — paper
#    3 — lizard
#    4 — scissors
#    if name does not match any of the strings above return -1

    # convert name to lower case before comparision
    if type( name ) == str:
        name_lower = name.lower()
    else:
        return -1

    if name_lower == "rock":
        return 0
    elif name_lower == "spock":
        return 1
    elif name_lower == "paper":
        return 2
    elif name_lower == "lizard":
        return 3
    elif name_lower == "scissors":
        return 4
    else:
        return -1
    
def number_to_name( number ):
# convert number to name:
#    0 — rock
#    1 — Spock
#    2 — paper
#    3 — lizard
#    4 — scissors

    # use a list to store the strings
    names = [ "rock", "Spock", "paper", "lizard", "scissors" ]

    # if the number is out of range, return None
    if type( number ) != int or number < 0 or number > 4:
        return None

    # if the number is between 0 and 4, return the match string
    return names[ number ]
    
def rpsls( player_choice ):
    # print a blank line to separate consecutive games
    print( "" )
    
    # convert the player's choice to player_number
    player_number = name_to_number( player_choice )

    # stop the game if there is something wrong with arguments
    if player_number == -1:
        print( "Game over for wrong argument!" )
        return None

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange( 0, 5 )
    
    # convert comp_number to comp_choice
    comp_choice = number_to_name( comp_number )
    
    # stop the game if the computer doesn't work well
    if comp_choice == None:
        print( "Game over for computer fatal error" )
        return None
    
    # print choices from player and computer
    print( "Player chooses " + player_choice )
    print( "Computer chooses " + comp_choice )
    
    # if choices are same, the result is a draw and end the programme
    if player_number == comp_number:
        print( "Player and computer tie!" )
        return
    
    # according to Professor Joe Warren's hints, using the wheel to judge the items
    # when it is counterclockwise, the item will beat the nearest 2 ones
    # use mod function to acommplish it
    if ( player_number - comp_number ) % 5 <= 2:
        Winner = "Player"
    else:
        Winner = "Computer"
    print( Winner + " wins!" )
    return

#test coding
rpsls( number_to_name( 0 ) )
rpsls( number_to_name( 1 ) )
rpsls( number_to_name( 2 ) )
rpsls( number_to_name( 3 ) )
rpsls( number_to_name( 4 ) )
#rpsls( number_to_name( 3.5 ) )
#print( "Testing" )
#print( number_to_name( 1 ) )
#print( name_to_number( "paper" ) )
