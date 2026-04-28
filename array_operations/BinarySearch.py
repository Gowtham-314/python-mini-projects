"""---Array element Search in Python Using an NumPy Library---"""

#Program to Search a element in an array using NumPy.

#    Binary Search Algorithm

from numpy import *

class BinarySearch:
    
    def array_input(self):
        try:
            self.my_array=array(input("Enter elements separated by spaces: ").split(),int)
            # Binary search assumes sorted order; keep a sorted copy for searching.
            self.my_array=sort(self.my_array)
        except:
            print("Invalid input. Please enter integers separated by spaces.")
            exit()
            
    def search_ele(self,ele):
        if self.my_array.size==0:
            print("Array is empty.")
            return
        beg=0
        end=len(self.my_array)-1
        while beg<=end:
            mid=(beg+end)//2
            if self.my_array[mid]==ele:
                print(f"Element {ele} found at position: {mid}")
                return
            elif self.my_array[mid]<ele:
                beg=mid+1
            else:
                end=mid-1
        print("Element not found in the array.")


search=BinarySearch()
search.array_input()
element=int(input("Enter the element to search: "))
search.search_ele(element)