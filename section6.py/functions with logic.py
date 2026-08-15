#functions with logic

2%2
print(2%2) #0 even
print(3%2) #1 odd
print(20%2) #0 even

#checking the no is even or odd
print(20%2==0) #true
print(21%2==0) #false

#checking the even number
def even_check(number):
   result= number%2==0
   return result
even_check(20)
print (even_check(20))  #True
print(even_check(51))   #False

#or
def even_check(number):
   return number%2==0
print (even_check(32))  #true

#Return true if any number is even inside a list 
def check_even_list(num_list):
   for number in num_list:
    if number % 2 == 0:
       return True
    else:
       pass
print(check_even_list([1,3,5])) #none
print(check_even_list([2,4,5])) #true
#if any even then it returns true

def check_even_list(num_list):
   for number in num_list:
    if number % 2 == 0:
       return True
    else:
       pass    
   return False #if the reurn false comes in order of rt then its not crct
print(check_even_list([1,2,3])) #true
print(check_even_list([1,3,5])) #false

def check_even_list(num_list):
   even_numbers = []
   for number in num_list:
      if number % 2 == 0:
         even_numbers.append(number)
      else:
         pass
   return even_numbers
print(check_even_list([1,2,3,4,5]))
print(check_even_list([1,3,5]))  #[]