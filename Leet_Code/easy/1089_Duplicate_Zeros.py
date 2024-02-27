"""
Given a fixed-length integer array arr, duplicate 
each occurrence of zero, shifting the remaining 
elements to the right.

Note that elements beyond the length of the original 
array are not written. Do the above modifications to 
the input array in place and do not return anything.

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]

Constraints:

  1 <= arr.length <= 104
  0 <= arr[i] <= 9

Takeaway:

  Keep it simple.


"""
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        res = []
        
        for elem in arr:
            if elem != 0:
                res.append(elem)
            else:
                res.append(elem)
                res.append(elem)
        
        for j in range(len(arr)):
            arr[j] = res[j]

            
    def duplicateZeros_(self, arr: List[int]) -> None:
        # with while loop 
        x=0
        while len(arr)>x:
            if arr[x]==0:
                arr.insert(x+1,0)
                x+=2
                arr.pop(-1)
                continue
            x+=1

    def duplicateZeros__(self, arr: List[int]) -> None:
        # with enumerate
        # incrementing index as we go
        # i dont like it
        tmp = []
        i = 0
        n = len(arr)
        for (i,val) in enumerate(arr):
            if i>n:
                break
            tmp.append(val)
            i += 1
            if val==0:
                tmp.append(val)
                i += 1
    
        for j in range(len(arr)):
            arr[j] = tmp[j]
