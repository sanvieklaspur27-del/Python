#lamda expressions
def square(num):    #1
    return num**2
my_nums=[1,2,3,4,5]
for item in map(square,my_nums):
 print(item)  #1,4,9,16,25

 print(list(map(square,my_nums))) #[1,4,9,16,25]

 def splicer(mystring):
    if len(mystring)%2==0:
       return'EVEN'
    else:
       return mystring[0]
names=['Anddy', 'sanii','kityya']
list(map(splicer,names))
print(list(map(splicer,names)))

def check_even(num):   #2
   return num%2==0
mynums=[1,2,3,4,5,6]
list(filter(check_even,mynums))
print(list(filter(check_even,mynums))) #[2,4,6]
for n in filter (check_even,mynums): #2,4,6 in vertical
   print(n)

def square(num):    #3
   result=num**2
   return result
square(3)
print(square(3)) #9
#or
def square(num):
   return num ** 2

square=lambda num: num**2   #3
square(6)
print(square(6))  #36

list(map(lambda num:num**2,mynums)) #[1,4,9,16,25,36]
print(list(map(lambda num:num**2,mynums)))    #1

list(filter(lambda num:num%2==0,mynums)) #[2,4,6]
print(list(filter(lambda num:num%2==0,mynums)))  #2

names=['Andy','Evey','Sanii']
print(list(map(lambda x:x[0],names)))