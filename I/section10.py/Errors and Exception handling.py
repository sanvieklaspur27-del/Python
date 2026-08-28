def add(n1,n2):
    print(n1+n2)
add(10,20)


try:
    # WANT TO ATTEMPT THIS CODE
    # MAY HAVE AN ERROR
    result=10+10
except:
    print("Hey it looks like you aren't adding correctly!")

try:
    result = 10 + 10
except:
    print("Hey it looks u aren't adding correctly")
print(result)

try:
    f= open('testfile','r')
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print('Hey you have an OS Error')
finally:
    print("I always run")   # I always run and os error


try:
    f= open('testfile','r')
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except:
    print('All other exceptions!')
finally:
    print("I always run")    # ALL OTHER EXCEPTIONS AND I ALWAYS RUN

def ask_for_int():
    while True:
     try:
        result=int(input("please provide number:"))
     except:
        print("Whoops! That is not a number")
        continue
     else:
         print("Yes thank you")
         break
     finally:
        print("End of try/except/finally")
        print("I will always run at the end!")  # ALWAYS RUN UNTIL THEY GIVE INT NUMBER

ask_for_int()

# 1EXAMPLE OF TO SOLVE A PROBLEM

try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("General Error! Watch out!")


#  2EXAMPLE OF TO SOLVE A PROBLEM

try:
    x=5
    y=0
    z=x/y
except:
    print("Error!!")
finally:
    print("All done")

#3 EXAMPLE OF TO SOLVE A PROBLEM

def ask():
    while True:
        try:
            n=int(input("Enter a number"))
        except:
            print("pls try again! \n")
            continue
        else:
            break

    print("YouR number squared is:")
    print(n**2)
ask()











