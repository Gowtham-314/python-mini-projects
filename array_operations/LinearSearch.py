"""---Array element Search in Python Using an NumPy Library---"""

#Program to Search a element in an array using NumPy.

#    Linear Search Algorithm

from numpy import *

class LineraSearch:
    
    def array_input(self):
        try:
            global my_array
            my_array=array(input("Enter elements separated by spaces: ").split(),int)
        except:
            print("Invalid input. Please enter integers separated by spaces.")
            exit()
            
    def search_ele(self,ele):
        for i in range(len(my_array)):
            if my_array[i]==ele:
                print(f"Element {ele} found at position: {i}")
                return
        print("Element not found in the array.")
        
    
    
search=LineraSearch()
search.array_input()
element=int(input("Enter the element to search: "))
search.search_ele(element)