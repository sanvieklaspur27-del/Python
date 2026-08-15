#while loops

x=0
while x<5:
    print(f'The current value of x is {x}')
    x=x+1  #0,1,2,3,4 or x+=1
else:
    print( 'its not true')

#break,continous,pass
x=[1,2,3]
for item in x:
  pass  #does ntg
  print('end of myscript')

mystring='sammy'
for letter in mystring:
   print (letter) #s,a,m,m,y

for letter in mystring:
   if letter =='a':
      continue  #goes back of the loop
   print (letter) #s,m,m,y

for letter in mystring:
   if letter =='a':
      break   
   print (letter) #s

x=0
while x<5:
   print(x)
   x+=1   #0,1,2,3,4

   x=0
while x<5:
   if x==2:
      break
   print(x)
   x+=1    # 0,1