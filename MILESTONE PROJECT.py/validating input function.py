
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
