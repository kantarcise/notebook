"""
Given an array arr of integers, check if there exist 
two indices i and j such that :

    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]
 
Example 1:

    Input: arr = [10,2,5,3]
    Output: true
    
    Explanation: For i = 0 and j = 2, 
            arr[i] == 10 == 2 * 5 == 2 * arr[j]

Example 2:

    Input: arr = [3,1,7,11]
    Output: false
        
    Explanation: There is no i and j that 
        satisfy the conditions.
 

Constraints:

    2 <= arr.length <= 500
    -10^3 <= arr[i] <= 10^3

Takeaways:

    Using sets is a wonderful tool here.

"""
class Solution:
    def checkIfExist_(self, arr: list[int]) -> bool:
        # a brute force would be linear search
        n = len(arr)
        for i in range(n) :
            for j in range(i) :
                # up until i, check every position
                if (arr[i]==2*arr[j]) or (arr[j]==2*arr[i]) :
                    return True 
        return False    
    
    def checkIfExist(self, arr: list[int]) -> bool:
        # better solution would be using a set
        seen = set()
        
        for i in range(len(arr)):
            # have we encountered before?
            if arr[i] * 2 in seen:
                return True
            # conditions
            elif arr[i] % 2 == 0 and arr[i] / 2 in seen:
                return True
            # just add to set
            else:
                seen.add(arr[i])
        return False

sol = Solution()
print(sol.checkIfExist(arr = [10,2,5,3]))
print(sol.checkIfExist(arr = [3,1,7,11]))
