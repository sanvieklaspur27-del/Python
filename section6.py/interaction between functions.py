#ineraction btw functions

example=[1,2,3,4,5,6,7,8]
from random import shuffle  #shuffle funct
shuffle(example)
print(example)
#or
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
result=shuffle_list(example)
print(result)

#game
mylist=['','0','']
shuffle_list(mylist)  #shuffle
print(mylist)
def player_guess():    #guessing
    guess=''
    while guess not in['0','1','2']:
     guess=input("pick a number:0,1, or 2")
    return int(guess)
print(player_guess())      #picka no:0,,1,2[1]--1
print(player_guess())       #0---0
 #checking
def check_guess(mylist, guess):
    if mylist[guess]=='0':  #checking
       print('correct!')
    else:
       print('wrong guess!')
       print(mylist)
# INITIAL LIST
mylist=['','0','']
# SHUFFLE LIST
mixedup_list=shuffle_list(mylist)
# USER GUESS
guess=player_guess()
# CHCEK GUESS  
check_guess(mixedup_list,guess) 