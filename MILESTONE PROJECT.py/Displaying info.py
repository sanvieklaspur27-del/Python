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