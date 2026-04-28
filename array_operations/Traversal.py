""""---Array Traversal in Python Using an NumPy Library---"""

#Program to Find the frequency of ellements in an array using NumPy.

from numpy import *

def find_freq(arr,element):
    freq=0
    for i in arr:
        if i==element:
            freq+=1
    return freq
try:
    my_array=array(input("Enter elements separated by spaces: ").split(),int)
except:
    print("Invalid input. Please enter integers separated by spaces.")
    exit()
    
search_ele=int(input("Enter the element to find its frequency: "))
frequency=find_freq(my_array,search_ele)
if frequency>0:
    print("The Frequency of",search_ele,"in the array is:",frequency)
else:
    print("Element not found in the array.")
