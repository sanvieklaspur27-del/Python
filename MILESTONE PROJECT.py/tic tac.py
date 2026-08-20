#tic tac


def display_board(board):
    
    print('  |  |')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('  |  |')
    print('--------')
    print('  |  |')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('  |  |')
    print('--------')
    print('  |  |')
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('  |  |')
test_board=['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)

def player_input():

    '''
    OUTPUT = (player 1 marker, player 2 marker)
    '''

    marker=''

   #KEEP ASKING PLAYER 1 TO CHOOOSE X TO O
    while marker!='X' and marker!='O':
        marker=input('Player1: Choose X or O: ').upper()
    if marker=='X':
        return('X','O')
    else:
        return('O','X')

player1_marker , player2_marker = player_input()
print(player1_marker , player2_marker)
player1_marker

def place_marker(board,marker,position):
    board[position]=marker
test_board 
print(test_board)
place_marker(test_board,'s',9)
display_board(test_board)

def win_check(board,mark):
    #WIN TIC TAC TOE?
    return((board[7]==mark and board[8]==mark and board[9]==mark) or  
    (board[4]==mark and board[5]==mark and board[6]==mark) or
    (board[1]==mark and board[2]==mark and board[3]==mark) or 
    (board[7]==mark and board[4]==mark and board[1]==mark) or
    (board[8]==mark and board[5]==mark and board[2]==mark) or 
    (board[9]==mark and board[6]==mark and board[3]==mark) or
    (board[7]==mark and board[5]==mark and board[3]==mark) or
    (board[9]==mark and board[5]==mark and board[1]==mark))
display_board(test_board)
win_check(test_board,'X')

import random
def choose_first():

    flip=random.randint(0,1)
    if flip==0:
        return 'player1'
    else:
        return 'player2'
    
def space_check(board,position):

     return board[position]==''

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False      # if i ahd a space the board looks normal
        # BOARD IS FULL IF WE RETURN TRUE
        return True

def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position= int(input('choose a position:(1-9)'))
    return position

def replay():
    choice= input("play again? Enter yes or no")
    return choice=='yes'

#logics
 
#WHILE LOOP TO KEEP RUNNING THE GAME
print('Welcome to Tic Tac Toe')

while True:
    #play the game
    ##SET EVERYTHING UP (BOARD , WHOS FIRST,CHOOSE MARKERS X,O)
    the_board=['']*10
    player1_marker,player2_marker=player_input()

    turn=choose_first()
    print(turn+'will go first')

    play_game=input('Ready to play? y or n?')

    if play_game=='y':
       game_on=True
    else:
       game_on=False



    ##GAME PLAY
    while game_on:
     if turn=='player1':

         ##SHOW THE BOARD
         display_board(the_board)
         #CHOOSE THE POSITION
         position=player_choice(the_board)

         #PLACE THE MARKER ON THE POSITION
         place_marker(the_board,player1_marker,position)

         # CHECK IF THEY WIN
         if win_check(the_board,player1_marker):
             display_board(the_board)
             print('PLAYER 1 HAS WON!!')
             game_on=False
         else:
          if full_board_check(the_board):
              display_board(the_board)
              print("TIE GAME!")
              break
          else:
            turn = 'Player 2'
     else:
         
         ##SHOW THE BOARD
         display_board(the_board)
         #CHOOSE THE POSITION
         position=player_choice(the_board)

         #PLACE THE MARKER ON THE POSITION
         place_marker(the_board,player2_marker,position)

         # CHECK IF THEY WIN
         if win_check(the_board,player2_marker):
             display_board(the_board)
             print('PLAYER 2 HAS WON!!')
             game_on=False
         else:
          if full_board_check(the_board):
              display_board(the_board)
              print("TIE GAME!")
              break
          else:
            turn = 'Player 1'
         
     if not replay():
         break


# BREAK OUT OF THE WHILE LOOP ON replay()

  










    
    