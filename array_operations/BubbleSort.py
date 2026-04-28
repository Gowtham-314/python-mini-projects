"""---Array Sort in Python Using an NumPy Library---"""

#Program to Sorting a elements in an array using NumPy.

#    Bubble Sort Algorithm

from numpy import *

class BubbleSort:
    
    def array_input(self):
        try:
            self.my_array=array(input("Enter elements separated by spaces: ").split(),int)
        except:
            print("Invalid input. Please enter integers separated by spaces.")
            exit()
    
    def array_sort(self):
        
        n = len(self.my_array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.my_array[j] > self.my_array[j + 1]:
                    self.my_array[j], self.my_array[j + 1] = self.my_array[j + 1], self.my_array[j]


arr_sort=BubbleSort()
arr_sort.array_input()
print("Array Before the Sort : ",arr_sort.my_array)
arr_sort.array_sort()
print("\nArray After the Sort : ",arr_sort.my_array)