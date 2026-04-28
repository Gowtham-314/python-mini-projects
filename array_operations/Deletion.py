""""---Array Deletion in Python Using an NumPy Library---"""

#Program to Delete a element to an array using NumPy.

from numpy import *

class ArrayDeletion:


    def array_input(self):
        try:
            self.my_array=array(input("Enter elements separated by spaces: ").split(),int)
        except:
            print("Invalid input. Please enter integers separated by spaces.")
            exit()
            
    def delete_ele(self,pos):
        del_ele=self.my_array[pos]
        for i in range(pos,len(self.my_array)-1):
            self.my_array[i]=self.my_array[i+1]
        self.my_array=delete(self.my_array,len(self.my_array)-1)                #deleting the last element.
        print(f"Deleted element: {del_ele}")
        
array_del=ArrayDeletion()
array_del.array_input()
length=len(array_del.my_array)
position=int(input(f"Enter the position to delete the element (0 to {length-1}): "))
if position<0 or position>=length:
    print(f"Invalid position. Please enter a position between 0 and {length-1}.")
    exit()
array_del.delete_ele(position)
print(f"\nArray after deletion: {array_del.my_array}")