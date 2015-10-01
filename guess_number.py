# mini-project: guess the number
# date: 2015-08-02, sorry for the late
# author: yubi
# email: yubi@foxmail.com
import simplegui
import random
import math

# define global argument secret_number to store the answer
# define global argument mycount to count the how many times to guess
# define global argument myrang to set range for 0~100 or 0~1000 guess
# define global argument times for the judge
secret_number = 0
mycount = 0
myrange = 100
times = int( math.ceil( math.log( myrange, 2 ) ) )

# define functions

# define the answer when the play lose the game
def show_me_answer():
    # encourage the player
    print( "It's just a game, come on buddy!" )
    # show the range
    print( "This is a game to guess number from 0 to " + str( myrange ) )
    # show the secret_number
    print( "The secret number is: " + str( secret_number ) )
    # maybe the computer will occur some errors
    if( secret_number < 0 or secret_number >= myrange ):
        print( "Here is something wrong, and I will lose the game either ^_^" )
        return
    # initialize statistics
    mycount = 1
    myguess = -1
    low = 0
    high = myrange
    # show the binary search process of approaching the answer
    while( myguess != secret_number ):
        # always choose the middle number average of range
        myguess = int( math.floor( ( low + high ) / 2 ) )
        print( "Round " + str( mycount ) + ": I will guess " + str( myguess ) )
        # when you search the right number, it's done
        if( myguess == secret_number ):
            print( "It's the answer!" )
        # if our guess is bigger than secret_number, we cut off the higher half     
        elif( myguess > secret_number ):
            high = myguess
            mycount += 1
            print( "It's higher, and we swith range to [ " + str( low ) + " ~ " + str( high ) + " )" )
        # if our guess is smaller than secret_number, we cut off the lower half
        elif( myguess < secret_number ):
            low = myguess
            mycount +=1
            print( "It's lower, and we swith range to [ " + str( low ) + " ~ " + str( high ) + " )" )
        else:
            print( "You shall not pass ~~~~~~" )
    print( "Have a fun, and start a new one!" )
    return

# define event handler input_guess takes the input string guess, converts it to an integer, and prints out a message
def input_guess( guess ):
    global mycount
    #print( "times, mycount", times, mycount )
    # show the strategy and start a new game for the player who lost the game
    if( mycount >= times ):
        print( "Haha, you lose the game!" )
        show_me_answer()
        newgame()
        return
    # check the input number is a digital number or not
    # show message and ignore the wrong input
    # else calculate the count for remaining guesses
    if( not guess.isdigit() ):
        print( "Is not a digital number!" )
        return
    else:
        myguess = int( guess )
        mycount += 1
    """
    if( myguess < 0 or myguess >= myrange ):
        print( "Your number is out of range!" )
    """
    print( "Guess was " + guess )
    # compares the entered number to secret_number
    # enter_number == secret_number: Correct, and start a new game
    # enter_number > secret_number: Higher
    # enter_number < secret_number: Lower
    if( myguess == secret_number ):
        print( "Correct" )
        newgame()
    elif( myguess > secret_number ):
        print( "Higher" )
    elif( myguess < secret_number ):
        print( "Lower" )
    
# define function new_game that initializes a global variable secret_number
def newgame():
    global mycount, times, secret_number
    # reset count times to zero
    mycount = 0
    # set the maximum times for the game
    times = int( math.ceil( math.log( myrange, 2 ) ) )
    # set the secret_number as a random for the answer
    secret_number = random.randrange( 0, myrange )
    #print( "secret_number is: " + str( secret_number ) )

# def the game range from 0 to 100
def newgame100():
    global myrange
    # set the range
    myrange = 100
    # start a new game
    newgame()

# def the game range from 0 to 1000
def newgame1000():
    global myrange
    # set the range
    myrange = 1000
    # start a new game
    newgame()

# create the frame
# add two buttons to the frame, one for game 0~100 and the other for game 0~1000
frame = simplegui.create_frame( "Guess the number", 300, 300)
frame.add_button( "Range is [0,100)", newgame100, 120 )
frame.add_button( "Range is [0,1000)", newgame1000, 120 )
# add input to the frame, covert the input number
frame.add_input( "Guess: ", input_guess, 120 )


# test and debug
#input_guess( 50 )
#input_guess( "50" )
#newgame()

    















digit_check

    # Check the input is a number 
    if( not t.isdigit() ):
        # If the input is digit, check it is a float
        # split the string by decimal point
        splitlist = t.split( '.' )
        # If it is a float, it can be split into 2 parts of digit number
        if( len( splitlist ) == 2 and splitlist.pop().isdigit() and splitlist.pop().isdigit() ):
            operand = float(t)
            output()
        else:
            print( "It's not a number" )            
    else:    
        operand = int(t)
        output()
    

	
	
    if( operand == 0 ):
        print( "divide number by zero" )
        return


	if( t[0] == '-' ):
        t = t.replace( '-', '', 1 )
        sign = -1
    else:
        sign = 1
