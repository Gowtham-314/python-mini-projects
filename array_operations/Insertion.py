""""---Array Insertion in Python Using an NumPy Library---"""

#Program to Insert a element to an array using NumPy.

from numpy import *

class ArrayInsertion:
    
    def array_input(self):
        try:
            global my_array
            my_array=array(input("Enter elements separated by spaces: ").split(),int)
        except:
            print("Invalid input. Please enter integers separated by spaces.")
            exit()
    
    def insert_ele(self,pos,ele):
        for i in range(length-1,pos-1,-1):
            my_array[i+1]=my_array[i]
        print(my_array[pos-1])
    
arr_insert=ArrayInsertion()
arr_insert.array_input()
global length
length=len(my_array)
position=int(input(f"Enter the position to insert the element (0 to {length}): "))

if position<0 or position>length+1:
    print(f"Invalid position. Please enter aposition between 0 and {length}.")
    exit()
    
element=int(input("Enter the element to insert: "))
arr_insert.insert_ele(position, element)
print("Array after insertion:", my_array)