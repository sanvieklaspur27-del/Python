#for loops

mylist=[1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print(num)
for jelly in mylist:
    print(jelly)
for jelly in mylist:
    print('hello')       #hello is printed 10 times

#check for even
for num in mylist:
    if num % 2==0:
     print(num)        # 2,4,6,8,10
    else:
     print(f'odd Number:{num}') #1,3,5,7,9

#0+1=1,1+2=3,3+3=6
list_sum=0
for num in mylist:   
   list_sum=list_sum+num
print(list_sum)   #55 , if space then 1,3,6,10..55

#string
mystring='hello word'
for letter in mystring:
   print(letter)   #h,e,l,l,o  w,o,r,l,d

#tuples
tup=(1,2,3)
for item in tup:
   print(item)  #1,2,3

#lists
mylist=[(1,2),(3,4),(5,6)]
print (len(mylist))  #3
for item in mylist:
 print(item)       #(1,2)(3,4)(5,6)

for (a,b) in mylist:
   print(a)
   print(b)       #1,2,3,4,5,6

#dict
d={'k1':1,'k2':2,'k3':3}
for item in d:
   print(item)  #k1,k2,k3
for item in d.items():
   print(item)  #(k1,1),(k2,2),(k3,3)