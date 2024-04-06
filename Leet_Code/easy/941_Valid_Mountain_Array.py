"""
Given an array of integers arr, return true if 
and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
    arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:

    Input: arr = [2,1]
    Output: false

Example 2:

    Input: arr = [3,5,5]
    Output: false

Example 3:

    Input: arr = [0,3,2,1]
    Output: true

Constraints:

    1 <= arr.length <= 10^4
    0 <= arr[i] <= 10^4

Takeaway:

    Use the conditions that you are given to reach the answer!

"""

class Solution:
  
    def validMountainArray_(self, arr: List[int]) -> bool:
        # This works
        # base case
        if len(arr) < 3:
            return False
        
        # it should increase, and it should decrease
        # strictly
        peak, valley = 0, 0
        
        # picture two persons climbing the mountain and 
        # trying to arrive at the same peak
        for i in range(1, len(arr) - 1):
            if arr[i - 1] < arr[i] > arr[i + 1]:
                # we are looking to find a single peak
                peak += 1
            if arr[i - 1] >= arr[i] <= arr[i + 1]:
                # we do not want any valleys
                valley += 1
                
        return peak == 1 and valley == 0
    
    def validMountainArray(self, arr: List[int]) -> bool:
        # Another approach
        
        # trust the arr to be a valid mountain array
        index = 0
        
        # strictly increasing
        while index+1 < len(arr) and arr[index+1] > arr[index]:
            index += 1
        
        # now the index at peak
        
        # peak element can not be at beginning 
        # or 
        # end of the arr
        if index == 0 or index == len(arr) - 1:
            return False
        
        # from the peak, we should be 
        # strictly decreasing
        while index+1 < len(arr) and arr[index+1] < arr[index]:
            index += 1
        
        # two cases may arise:
        # 1. valid mountain array, index has reached the end
        # 2. not valid mountain array, index has not reached the end
        return index == len(arr)-1
