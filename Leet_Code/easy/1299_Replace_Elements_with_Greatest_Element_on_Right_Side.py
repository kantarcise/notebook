"""
Given an array arr, replace every element in that array with the 
greatest element among the elements to its right, and 
replace the last element with -1.

After doing so, return the array.

Example 1:

    Input: arr = [17,18,5,4,6,1]
    Output: [18,6,6,6,1,-1]
    Explanation: 
        - index 0 --> the greatest element to the right of index 0 is index 1 (18).
        - index 1 --> the greatest element to the right of index 1 is index 4 (6).
        - index 2 --> the greatest element to the right of index 2 is index 4 (6).
        - index 3 --> the greatest element to the right of index 3 is index 4 (6).
        - index 4 --> the greatest element to the right of index 4 is index 5 (1).
        - index 5 --> there are no elements to the right of index 5, so we put -1.

Example 2:

    Input: arr = [400]
    Output: [-1]
    Explanation: There are no elements to the right of index 0.
 
Constraints:

    1 <= arr.length <= 10^4
    1 <= arr[i] <= 10^5

Takeaway:

    To switch values, use tuples!

"""
class Solution:
    def replaceElements_(self, arr: List[int]) -> List[int]:
        # works, but time limit exceeded
        
        # for every index, do the operation
        for i in range(len(arr)-1):
            arr[i] = max(arr[i+1:])
        arr[-1] = -1
        
        return arr
    
    def replaceElements__(self, arr: List[int]) -> List[int]:
        # this is not working correctly
        # just off by one
        
        # we do not have to calculate max each time
        
        # arr = [17,18,5,4,6,1]
        # resulting:
        # arr = [18,6,6,6,1,-1]
        # compare elements one by one
        
        temp = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            print(temp, "temp now")
            arr[i] = max(temp, arr[i])
            print(f"current max {arr[i]}")
            temp = arr[i]
            print(f"Temp after {temp}")
        
        arr[-1] = 1
        
        return arr
    
    def replaceElements(self, arr: List[int]) -> List[int]:
        # IF you want to switch values
        # USE TUPLE UNPACKING
    
        # we do not have to calculate max each time
    
        # arr = [17,18,5,4,6,1]
        # resulting:
        # arr = [18,6,6,6,1,-1]
        # compare elements one by one
    
        temp = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            arr[i], temp = temp, max(temp, arr[i])
        
        arr[-1] = -1
        
        return arr
