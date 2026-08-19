#Displaying information
print([1,2,3])  #[1,2,3]
print([4,5,6])
print([7,8,9])

def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

row1 = ['','','']
row2 = ['','','']
row3 = ['','','']

display(row1,row2,row3)

row2[1] ='X'
display(row1,row2,row3)


#Accepting user input
input("please enter a value:")
print(input("please enter a value:"))
result=print(input("please enter a value:"))

result=input("Enter a value:")

#result_int=int(result)#

position_index=int(input("choose an index position: "))
type(position_index)
(row2[position_index])
result=input("Enter a Number:")
print(2+2)
#input=("Enter a number:")
print(100+100)

#Validating input function

def user_choice():
    choice = input("please enter a number(0-10): ")
 #   return int(choice)
#user_choice()

some_value='100'
some_value.isdigit()
print(some_value.isdigit())  #True

int(some_value)
print(int(some_value))   #100

 #again and again asking!
def user_choice():
    choice='WRONG'
    while choice.isdigit()==False:


     choice = input("please enter a number(0-10): ")
     if choice.isdigit()==False:
        print("sry that is not a digit!")

    return int(choice)

user_choice()

result= 'Wrong value'
acceptable_values=[0,1,2]
print(result in acceptable_values) #False
print(result not in acceptable_values) #True


def user_choice():

    #VARIABLES

    #Initial 
    choice='WRONG'
    acceptable_range=range(0,10)
    within_range=False

    #TWO COND TO CHECK
    #DIGIT OR WITHIN_RANGE == FALSE

    while choice.isdigit()==False or within_range==False:


     choice = input("please enter a number(0-10): ")

     #Digit check
     if choice.isdigit()==False:
        print("sry that is not a digit!")

        #Range check
     if choice.isdigit()==True:
        if int(choice) in acceptable_range:
          within_range=True
        else:
          print(" sry ur out of acceptable range(0-10)")
          within_range=False

    return int(choice)

#simple user interaction

game_list=[0,1,2]
def display_game(game_list):
   print("here is the crct list: ")
   print(game_list)
display_game(game_list)  #here is the crct list[0,1,2]

def position_choice():

    choice='wrong'

    while choice not in ['0','1','2']:
       choice=input("pick a position ('0','1','2'): ")
       if choice not in ['0','1','2']:
          print("sry, invalid choice!")
    return int(choice)

position_choice()

def replacement_choice(game_list,position):
   user_placement=input("type a string to place at position: ")
   game_list[position]=user_placement
   return game_list
replacement_choice(game_list,1)

def gameon_choice():

    choice='wrong'

    while choice not in ['Y','N']:
       
       choice=input("Keep playing? (Y or N) ")

       if choice not in ['Y','N']:
          print("sry,I don't understand, pls choose Y or N!")

    if choice=="Y":     
     return True
    else:
     return False

gameon_choice()

game_on = True
game_list = [0,1,2]

while game_on:
   display_game(game_list)
   position=position_choice()
   game_list=replacement_choice(game_list,position)
   display_game(game_list)
   game_on = gameon_choice()





























